import os, json, pandas as pd, hashlib
from difflib import get_close_matches
from docling.document_converter import DocumentConverter

# Setup directories
input_dir, success_dir, failed_dir = "input", "processed/success", "processed/failed"
os.makedirs(success_dir, exist_ok=True)
os.makedirs(failed_dir, exist_ok=True)
csv_file, json_path = "processed/output.csv", "colomnHeader.json"

if not os.path.exists(json_path):
    raise FileNotFoundError(f"Missing file: {json_path}")

# Load JSON config
header_config = json.load(open(json_path, "r", encoding="utf-8"))
unique_identifiers = header_config.get('unique_identifiers', ['hsn_sac_identifier'])
header_map = {s.strip().lower(): c for section, groups in header_config.items() 
              if section != 'unique_identifiers' for c, syns in groups.items() for s in syns}
all_synonyms = list(header_map.keys())

# Normalize headers
def normalize_headers(df, cutoff=0.6):
    if all(str(col).strip().isdigit() for col in df.columns): return None
    rename_map = {col: header_map.get(col.lower()) or header_map.get(
        get_close_matches(col.lower(), all_synonyms, n=1, cutoff=cutoff)[0], col)
        for col in df.columns if col.lower() in header_map or get_close_matches(col.lower(), all_synonyms, n=1, cutoff=cutoff)}
    return df.rename(columns=rename_map)

# Clear column_header fields
def edit_column_headers(obj, count=0):
    if isinstance(obj, dict):
        if obj.get("column_header") and "text" in obj and ":" in obj["text"]:
            obj["text"], count = "", count + 1
        for v in obj.values(): count = edit_column_headers(v, count)
    elif isinstance(obj, list): 
        for item in obj: count = edit_column_headers(item, count)
    return count

# Merge DataFrames
def merge_dataframes(dfs, unique_identifiers):
    clean_dfs = []
    for df in dfs:
        if df is None or all(str(c).strip().isdigit() for c in df.columns):
            continue
        mask = df.apply(lambda row: any('total' in str(row.get(c,'')).lower() for c in unique_identifiers + ['description']), axis=1)
        df_clean = df[~mask].astype(str).fillna('')
        if not df_clean.empty: clean_dfs.append(df_clean)
    if not clean_dfs: return pd.DataFrame()
    
    uid = next((col for col in unique_identifiers if all(col in df.columns for df in clean_dfs)), None)
    if not uid: return pd.concat(clean_dfs, ignore_index=True)
    merged = clean_dfs[0].set_index(uid)
    for df in clean_dfs[1:]: merged = merged.combine_first(df.set_index(uid))
    return merged.reset_index()

# Convert DataFrame to text
def dataframe_to_text(df):
    if df.empty: return ""
    widths = [max(len(str(c)), *(len(str(v)) for v in df[c])) for c in df.columns]
    header = "  ".join(f"{c:<{w}}" for c, w in zip(df.columns, widths))
    separator = "  ".join("-"*w for w in widths)
    rows = ["  ".join(f"{str(v):<{w}}" for v, w in zip(row, widths)) for row in df.values]
    return "\n".join([header, separator] + rows)

# Initialize CSV with required columns if not exists
if not os.path.exists(csv_file):
    pd.DataFrame(columns=['hash_for_invoice', 'invoice_no']).to_csv(csv_file, index=False)

# Process all PDFs
for pdf_file in os.listdir(input_dir):
    if not pdf_file.endswith('.pdf'): continue
    pdf_path = os.path.join(input_dir, pdf_file)
    output_txt_path = os.path.join("processed", f"{os.path.splitext(pdf_file)[0]}.txt")
    
    try:
        # Generate unique hash
        hash_for_invoice = hashlib.md5(pdf_file.encode()).hexdigest()
        
        # Read CSV to get next invoice number
        existing_df = pd.read_csv(csv_file)
        if 'invoice_no' in existing_df.columns and not existing_df.empty:
            last_invoice = pd.to_numeric(existing_df['invoice_no'], errors='coerce').max()
            invoice_no = str(int(last_invoice) + 1).zfill(8) if pd.notna(last_invoice) else '00000001'
        else:
            invoice_no = '00000001'
        
        # Process PDF
        doc = DocumentConverter().convert(pdf_path)
        doc_dict = doc.document.model_dump()
        edit_column_headers(doc_dict)
        doc.document = doc.document.__class__.model_validate(doc_dict)

        tables_dfs = []
        for t in doc.document.tables:
            try:
                df = t.export_to_dataframe(doc)
                df_norm = normalize_headers(df)
                if df_norm is not None: tables_dfs.append(df_norm)
            except: continue

        merged_df = merge_dataframes(tables_dfs, unique_identifiers)
        if merged_df.empty: raise ValueError("No valid data extracted")

        # Add hash and invoice number
        merged_df['hash_for_invoice'] = hash_for_invoice
        merged_df['invoice_no'] = invoice_no

        # Save text output
        text_content = dataframe_to_text(merged_df)
        with open(output_txt_path, 'w', encoding='utf-8') as f:
            f.write(text_content)

        # Append to CSV
        common_columns = merged_df.columns.intersection(existing_df.columns)
        merged_df = merged_df.reindex(columns=common_columns, fill_value='')
        combined_df = pd.concat([existing_df, merged_df], ignore_index=True)
        combined_df.to_csv(csv_file, index=False)

        # Move PDF to success folder
        os.rename(pdf_path, os.path.join(success_dir, pdf_file))
        print(f"Processed {pdf_file} successfully with invoice_no: {invoice_no}")

    except Exception as e:
        # Move PDF to failed folder
        os.rename(pdf_path, os.path.join(failed_dir, pdf_file))
        print(f"Failed to process {pdf_file}: {str(e)}")