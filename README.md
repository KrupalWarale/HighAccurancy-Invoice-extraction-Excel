# ⚡ High Accuracy Invoice Extraction to Excel

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel/network)
[![GitHub issues](https://img.shields.io/github/issues/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel/issues)
[![GitHub language](https://img.shields.io/github/languages/top/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel)

**A Python script for extracting data from invoices and outputting it to an Excel file.**

</div>

## 📖 Overview

This script extracts key invoice data and writes it into a structured Excel sheet. It targets high accuracy, possibly using docling library, with a custom json `colomnHeader.json` defining the output schema and headers.

## prototype

<p align="center">
  <img src="https://github.com/user-attachments/assets/1d6dc0a5-e3eb-4ab8-bae1-9f1006fdad94" alt="Invoice Example" width="400"/>
</p>


## ✨ Features

- **Invoice Data Extraction:** Processes invoice images or other data formats to extract relevant information.
- **Data Cleaning and Transformation:** Cleans and transforms extracted data to ensure accuracy and consistency.
- **Excel Output:** Generates a well-formatted CSV file (.csv) containing the extracted data.
- **Customizable Output:** (Likely) allows customization of output fields through configuration (needs confirmation via code review).
- **High Accuracy:** Aims for a high degree of accuracy in data extraction.


## 🛠️ Tech Stack
- **Python** – Core language  
- **pandas** – Data cleaning & tabular processing  
- **docling** – PDF parsing & table extraction  
- **hashlib** – Unique invoice hashing  
- **difflib** – Fuzzy string matching  
- **JSON** – Configurable field mapping (`colomnHeader.json`)  


### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel.git
   cd HighAccurancy-Invoice-extraction-Excel
   ```

2. **Install dependencies:** 
   ```bash
   pip install docling pandas
   ```

3. **Prepare Input:** Place your invoices pdf) in the `input` directory.  The format of the input data needs to be determined from the code.

4. **Run the script:**
   ```bash
   python main.py
   ```

5. **Check Output:** The processed data will be in the `output` directory in Excel format.


## 📁 Project Structure
```
├── input/                  # Input directory for PDF invoices
├── processed/
│   ├── success/            # Successfully processed PDFs
│   ├── failed/             # PDFs that failed processing
├── output/
│   ├── json/               # Extracted metadata in JSON format
│   ├── output.csv          # Consolidated table data
├── columnHeader.json       # Configuration file for header mappings
└── main.py                 # Main processing script
```

## ⚙️ Configuration

The `colomnHeader.json` file defines the structure of the output Excel file.  Its contents and format should be documented.  (Analyze `colomnHeader.json` and describe its structure and the role of each key.)



---

<div align="center">

**Made with ❤️ by KrupalWarale**

</div>
