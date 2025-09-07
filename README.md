⚡ High Accuracy Invoice Extraction to Excel
<div align="center">








Python script for accurate PDF invoice extraction to CSV/Excel.

</div>
📖 Overview

Extracts metadata & tables from PDF invoices, maps headers using JSON config, and outputs structured CSV & JSON. Handles varied formats with fuzzy matching and automatic error handling.

✨ Features

Auto PDF invoice processing

High accuracy via synonym & fuzzy matching

CSV output for Excel

Configurable field mapping (colomnHeader.json)

Metadata JSON export

Table merging & deduplication

Error handling with success/failed folders

🧠 Logic Overview

PDF Conversion: Convert PDFs with docling, extract text & tables.

Metadata Extraction: Find key-value pairs, clean headers, apply fuzzy matching.

Table Processing: Normalize headers, clean rows/columns.

Merging: Combine tables, remove duplicates, track invoices with hashes.

Output: Save CSV + JSON, manage processed files.

Benefits

Accurate, flexible, scalable, and traceable invoice handling.

🛠️ Tech Stack

Python, pandas, docling

hashlib (hashing), difflib (fuzzy matching)

🚀 Quick Start

Prerequisites: Python 3.9+, install deps:

pip install pandas docling


Run:

git clone https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel.git
cd HighAccurancy-Invoice-extraction-Excel
python main.py


Place PDFs in input/

Configure colomnHeader.json if needed

Outputs → output/output.csv + output/json/

Processed files → processed/success / processed/failed

📁 Project Structure
HighAccurancy-Invoice-extraction-Excel/
├── main.py
├── colomnHeader.json
├── input/
├── output/
│   ├── output.csv
│   └── json/
├── processed/{success,failed}

⚙️ Configuration

colomnHeader.json maps synonyms (item codes, HSN/SAC, description, qty, taxes, fees, etc.) → standardized names. Fuzzy matching ensures flexibility across invoice formats. Add/edit synonyms for better accuracy.

🤝 Contributing

Open issues or PRs welcome.

📄 License

MIT License.

📸 Sample Outputs

CSV Output
<img width="1517" height="590" alt="outputCsv" src="https://github.com/user-attachments/assets/a54ed951-988b-4f4d-8bd3-4af0a309c5b8" />

JSON Metadata Output
<img width="1167" height="644" alt="jsonOutput" src="https://github.com/user-attachments/assets/e20527f7-f1b2-480b-8f71-3403118bbb8f" />

<div align="center">

Made with ❤️ by KrupalWarale

</div>
