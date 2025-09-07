# ⚡ High Accuracy Invoice Extraction to Excel

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel/stargazers)

[![GitHub forks](https://img.shields.io/github/forks/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel/network)

[![GitHub issues](https://img.shields.io/github/issues/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel/issues)

[![GitHub language](https://img.shields.io/github/languages/top/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel)


**A Python script for high-accuracy invoice extraction from PDF files and conversion to CSV format.**

</div>

## 📖 Overview

Automates extraction of key info from PDF invoices (metadata and tables) into structured CSV for Excel. Handles invoice variations and improves accuracy using Python libraries for PDF processing and data manipulation.

## ✨ Features

- Automated PDF invoice processing
- High accuracy with intelligent field mapping
- CSV output for Excel
- Customizable field mapping via `colomnHeader.json`
- Metadata and table extraction
- Error handling with success/failed folders
- JSON metadata output

## 🧠 Logic Overview

### 📄 Step 1: PDF Document Conversion
- Uses `docling` to convert PDFs to structured documents.
- Extracts text content and table structures.

### 🔍 Step 2: Metadata Extraction
- **Text Parsing:** Scans invoice text for key-value pairs.
- **Header Processing:** Extracts relational data, clears redundant text, cleans column headers.
- **Fuzzy Matching:** Applies synonym matching for field variations.

### 📊 Step 3: Tabular Data Processing
- **Table Extraction:** Identifies and extracts tables from PDFs.
- **Header Normalization:** Maps headers to standardized names using `colomnHeader.json`.
- **Data Cleaning:** Filters irrelevant rows, removes empty columns, ensures consistency.

### 🔗 Step 4: Data Merging & Consolidation
- **Intelligent Merging:** Combines tables based on unique identifiers.
- **Deduplication:** Removes duplicates and merges overlapping data.
- **Invoice Tracking:** Generates unique hashes and sequential numbers.

### 💾 Step 5: Output Generation
- **CSV Export:** Saves consolidated data to `output.csv`.
- **JSON Metadata:** Stores key-value pairs as JSON files.
- **File Management:** Moves processed PDFs to success/failed folders.

### 🎯 Key Benefits
- **Accuracy:** Fuzzy matching reduces manual errors.
- **Flexibility:** Configurable field mapping for different formats.
- **Scalability:** Batch processing with automatic tracking.
- **Traceability:** Unique hashes and organized folders.

## 🛠️ Tech Stack

- **Python:** Core language.
- **pandas:** Data manipulation.
- **docling:** PDF processing.
- **hashlib:** Hash generation.
- **difflib:** Fuzzy matching.

## 🚀 Quick Start

### Prerequisites

- Python 3.x (tested on 3.9+).
- Install libraries: `pip install pandas docling`

### Installation

1. Clone repo: `git clone https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel.git`
2. Place PDFs in `input/`.
3. Configure `colomnHeader.json` as needed.
4. Run: `python main.py`
5. Outputs in `output/output.csv` and `output/json/`. Processed PDFs moved to `processed/success` or `processed/failed`.

## 📁 Project Structure

```
HighAccurancy-Invoice-extraction-Excel/
├── README.md
├── colomnHeader.json          # Field mapping config
├── main.py                    # Main script
├── input/                     # Input PDFs
├── output/                    # Output CSV & JSON
│   ├── output.csv
│   └── json/                  # Metadata JSONs
├── processed/                 # Processed files
│   ├── success/               # Successful PDFs
│   └── failed/                # Failed PDFs
```

## ⚙️ Configuration

`colomnHeader.json` maps invoice field synonyms to standardized names for accurate extraction. Contains table_unique_identifiers, line_item_table_headers, and charges_fees_table_headers. Adjust for your invoice formats.

## 🤝 Contributing

Contributions welcome! Open issues or PRs.

## 📄 License

MIT License.

## 📸 Sample Outputs

### Extracted CSV Output

<img width="1517" height="590" alt="outputCsv" src="https://github.com/user-attachments/assets/a54ed951-988b-4f4d-8bd3-4af0a309c5b8" />

### Extracted Metadata JSON Output

<img width="1167" height="644" alt="jsonOutput" src="https://github.com/user-attachments/assets/e20527f7-f1b2-480b-8f71-3403118bbb8f" />

---

<div align="center">

**Made with ❤️ by KrupalWarale**

</div>
