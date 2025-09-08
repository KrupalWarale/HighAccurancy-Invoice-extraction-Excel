
<img width="1919" height="1000" alt="doc" src="https://github.com/user-attachments/assets/22ea60f3-3c74-44ea-8b89-75f19d34e588" />


# ⚡ High Accuracy Invoice Extraction to Excel

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel/network)
[![GitHub issues](https://img.shields.io/github/issues/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel/issues)
[![GitHub language](https://img.shields.io/github/languages/top/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel)

<img width="1883" height="677" alt="{A1A2B484-B2B2-4983-93F7-6348154856F9}" src="https://github.com/user-attachments/assets/27257042-e958-4727-870a-4e61e5eea5a2" />





**A Python script for extracting data from invoices and outputting it to an CSV file.**

</div>

## 📖 Overview

This script extracts key invoice data and writes it into a structured CSV sheet. It targets high accuracy, possibly using docling library, with a custom json `colomnHeader.json` defining the output schema and headers.


## ✨ Features

- **Invoice Data Extraction:** Processes invoice images or other data formats to extract relevant information.
- **Data Cleaning and Transformation:** Cleans and transforms extracted data to ensure accuracy and consistency.
- **CSV Output:** Generates a well-formatted CSV file (.csv) containing the extracted data.
- **Customizable Output:** (Likely) allows customization of output fields through configuration (needs confirmation via code review).
- **High Accuracy:** Aims for a high degree of accuracy in data extraction.

## 🧠  Logical Overview

- Input PDFs: Scan all PDF files from `input` folder.
- PDF Conversion: Use Docling library to convert PDFs into objects containing raw text and tables.
- Metadata Extraction:
  - Extract key-value pairs from column headers (relational pairs).
  - Extract key-value pairs from raw text (`key: value`) including multi-line values.
  - Merge metadata from headers and text.
  - Save as JSON in `output/json` using a unique hash name.
**- Table Processing:**
   📂  JSON Format for Column Header Mapping
       
```

{
  "table_unique_identifiers": { 
    "item_identifier": [...], 
    "hsn_sac_identifier": [...], 
    "tax_identifier": [...], 
    "line_item_identifier": [...] 
  },
  "line_item_table_headers": { 
    "serial_number": [...], 
    "item_code": [...], 
    "description": [...], 
    "quantity": [...], 
    "unit_price": [...], 
    "net_amount": [...], 
    "gross_amount": [...] 
  },
  "charges_fees_table_headers": { 
    "charge_type": [...], 
    "charge_description": [...], 
    "charge_amount": [...], 
    "charge_rate": [...], 
    "charge_percentage": [...] 
  }
}
```
  - Convert tables to Pandas DataFrames.
  - Remove key-value pairs embedded in table colomn cells by editing object data return by docling itself.
  - Normalize headers using `colomnHeader.json` mapping(assigning headers name from colomnHeader.json with closest match using difflib library).
  - Merge tables using unique identifiers: item_identifier, hsn_sac_identifier, tax_identifier, line_item_identifier.
- Data Cleaning: Filter out irrelevant rows, totals, or duplicates; ensure consistent columns.
- CSV Output: Append merged DataFrame to `output/output.csv` with `hash_for_invoice` and sequential `invoice_no`.
- File Management: Move PDFs to `processed/success` if processed successfully, else `processed/failed`.
- Logging: Print or log success/failure messages for monitoring.






## 🛠️ Tech Stack
- **Python** – Core language  
- **pandas** – Data cleaning & tabular processing  
- **docling** – PDF parsing & table extraction  
- **hashlib** – Unique invoice hashing  
- **difflib** – Fuzzy string matching  
- **JSON** – Configurable field mapping (`colomnHeader.json`)  


### Usage & Installation

1. **Install dependencies:** 
   ```bash
   pip install docling pandas
   ```

2. **Prepare Input:** Place your invoices pdfs (multiple also allowed) in the `input` directory.  The format of the input data needs to be determined from the code.

3. **Run the script:**
   ```bash
   python main.py
   ```

4. **Check Output:** The processed data will be in the `output` directory in CSV format.


## ⚙️ Configuration

The `colomnHeader.json` file defines the structure of the output CSV file.  Its contents and format should be documented.  (Analyze `colomnHeader.json` and describe its structure and the role of each key.)



---
## Demo<table align="center" width="100%">
  <tr>
    <td width="50%" style="text-align: center;">
      <img src="https://github.com/user-attachments/assets/8bff875a-1f16-47e1-8108-95055d518191"  alt="outputCsv" style="width: 100%; height: 300px; object-fit: contain;"/>
    </td>
    <td width="50%" style="text-align: center;">
      <img  src="https://github.com/user-attachments/assets/aff572e7-a499-4da7-865d-7c1197795b36" alt="jsonOutput" style="width: 100%; height: 300px; object-fit: contain;"/>
    </td>
  </tr>
</table>




<div align="center">

**Made with ❤️ by KrupalWarale**

</div>
