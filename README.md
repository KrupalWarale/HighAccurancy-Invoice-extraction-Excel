# ⚡ High Accuracy Invoice Extraction to Excel

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel/stargazers)

[![GitHub forks](https://img.shields.io/github/forks/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel/network)

[![GitHub issues](https://img.shields.io/github/issues/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel/issues)

[![GitHub language](https://img.shields.io/github/languages/top/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel)


**A Python script for high-accuracy invoice extraction from PDF files and conversion to CSV format.**

</div>

## 📖 Overview

This Python script automates the extraction of key information from PDF invoices, including metadata and tabular data, and organizes it into a structured CSV file compatible with Excel. It's designed to handle variations in invoice layouts and improve data accuracy compared to manual entry. The script leverages Python libraries for PDF processing, data manipulation, and intelligent field mapping. This is particularly useful for businesses needing efficient and reliable invoice processing and accounting.

## ✨ Features

- **Automated PDF Invoice Processing:** Extracts key metadata and tabular data from PDF invoice files.
- **High Accuracy:** Uses intelligent field mapping and synonym matching to minimize errors inherent in manual data entry.
- **CSV Output:** Generates a neatly organized CSV file (.csv) that can be easily opened and analyzed in Excel.
- **Customizable Field Mapping:** Easily adaptable to different invoice formats through the `colomnHeader.json` configuration file.
- **Metadata Extraction:** Extracts relational key-value pairs from invoice text and headers.
- **Table Merging:** Intelligently merges multiple tables from invoices based on unique identifiers.
- **Error Handling:** Moves successfully processed files to a success folder and failed ones to a failed folder for easy tracking.
- **JSON Metadata Output:** Saves extracted metadata as JSON files for additional processing or reference.

## 🧠 Logic Overview

The script follows a comprehensive workflow to process PDF invoices efficiently:

### 📄 Step 1: PDF Document Conversion
- Uses the `docling` library to convert PDF files into structured document models.
- Extracts both text content and table structures from the invoices.

### 🔍 Step 2: Metadata Extraction
- **Text Parsing:** Scans the entire invoice text for key-value pairs (e.g., "Invoice No: 12345").
- **Header Processing:** Extracts relational data from column headers, clears redundant text, and cleans column header fields to improve accuracy.
- **Fuzzy Matching:** Applies intelligent synonym matching to handle variations in field names.

### 📊 Step 3: Tabular Data Processing
- **Table Extraction:** Identifies and extracts tables from the PDF using document structure analysis.
- **Header Normalization:** Maps table column headers to standardized names using the `colomnHeader.json` configuration.
- **Data Cleaning:** Filters out irrelevant rows (e.g., totals), removes empty or numeric-only columns, and ensures data consistency.

### 🔗 Step 4: Data Merging & Consolidation
- **Intelligent Merging:** Combines multiple tables based on unique identifiers (e.g., item codes, HSN/SAC).
- **Deduplication:** Removes duplicate entries and merges overlapping data.
- **Invoice Tracking:** Generates unique hashes and sequential invoice numbers for tracking.

### 💾 Step 5: Output Generation
- **CSV Export:** Saves the consolidated tabular data to `output.csv` for Excel compatibility.
- **JSON Metadata:** Stores extracted key-value pairs as JSON files in `output/json` for reference.
- **File Management:** Moves processed PDFs to `processed/success` or `processed/failed` folders.

### 🎯 Key Benefits
- **Accuracy:** Fuzzy matching and synonym handling reduce manual errors.
- **Flexibility:** Configurable field mapping adapts to different invoice formats.
- **Scalability:** Processes multiple invoices in batch with automatic tracking.
- **Traceability:** Unique hashes and organized folder structure for easy auditing.

## 🛠️ Tech Stack

- **Python:** Core programming language.
- **pandas:** Data manipulation and analysis library for handling tabular data.
- **docling:** Document processing library for extracting data from PDF files.
- **hashlib:** For generating unique hashes for invoice tracking.
- **difflib:** For fuzzy string matching to handle variations in field names.

## 🚀 Quick Start

### Prerequisites

- Python 3.x (tested on 3.9+). You may need to install it if you don't already have it. Instructions can be found at [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Install required libraries:
```bash
pip install pandas docling
```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel.git
   cd HighAccurancy-Invoice-extraction-Excel
   ```

2. **Place your PDF invoice files:** in the `input` directory.

3. **Configure field mapping:** Edit `colomnHeader.json` to match your invoice formats (see Configuration section below).

4. **Run the script:**
   ```bash
   python main.py
   ```

5. **Output:** The processed data will be saved in the `output` directory as a CSV file named `output.csv`. Extracted metadata will be saved as JSON files in `output/json`. Successfully processed PDFs will be moved to `processed/success`, and failed ones to `processed/failed`.

## 📁 Project Structure

```
HighAccurancy-Invoice-extraction-Excel/
├── README.md
├── colomnHeader.json          # Configuration for field mapping and synonyms
├── main.py                    # Main script for invoice processing
├── input/                     # Directory for input PDF invoice files
├── output/                    # Directory for output CSV file and JSON metadata
│   ├── output.csv
│   └── json/                  # Extracted metadata as JSON files
├── processed/                 # Directory for processed files
│   ├── success/               # Successfully processed PDFs
│   └── failed/                # Failed to process PDFs
```

## ⚙️ Configuration

The `colomnHeader.json` file is crucial for configuring the script to extract and map the desired data fields from invoices. This file contains:

- **table_unique_identifiers:** Lists of synonyms for unique identifiers like item codes, HSN/SAC codes, etc.
- **line_item_table_headers:** Mapping of various line item fields (description, quantity, price, taxes, etc.) with their possible synonyms.
- **charges_fees_table_headers:** Mapping for additional charges and fees fields.

The structure is a JSON object where keys are standardized field names and values are arrays of possible synonyms that might appear in invoices. The script uses fuzzy matching to map invoice fields to these standardized names, allowing it to handle variations in invoice formats.

Adjust this file as needed to reflect your specific invoice structures and add new synonyms for better matching accuracy.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📸 Sample Outputs

### Extracted CSV Output

<img width="1517" height="590" alt="outputCsv" src="https://github.com/user-attachments/assets/a54ed951-988b-4f4d-8bd3-4af0a309c5b8" />

### Extracted Metadata JSON Output

<img width="1167" height="644" alt="jsonOutput" src="https://github.com/user-attachments/assets/e20527f7-f1b2-480b-8f71-3403118bbb8f" />

---

<div align="center">

**Made with ❤️ by KrupalWarale**

</div>
