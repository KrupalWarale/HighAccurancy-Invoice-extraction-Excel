# ⚡ High Accuracy Invoice Extraction to Excel

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel/network)
[![GitHub issues](https://img.shields.io/github/issues/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel/issues)
[![GitHub language](https://img.shields.io/github/languages/top/KrupalWarale/HighAccurancy-Invoice-extraction-Excel?style=for-the-badge)](https://github.com/KrupalWarale/HighAccurancy-Invoice-extraction-Excel)

<table align="center" width="100%">
  <tr>
    <td width="33%" style="text-align: center;">
      <img src="https://github.com/user-attachments/assets/1d6dc0a5-e3eb-4ab8-bae1-9f1006fdad94" alt="First" style="width: 100%; height: 500px; object-fit: contain;"/>
    </td>

    <td width="32%" style="text-align: center;">
      <img src="https://github.com/user-attachments/assets/64bb712f-02ab-4f33-b916-1a7ac9243344" alt="Third" style="width: 150%; height: 500px; object-fit: contain;"/>
    </td>
  </tr>
</table>

**A Python script for extracting data from invoices and outputting it to an Excel file.**

</div>

## 📖 Overview

This script extracts key invoice data and writes it into a structured Excel sheet. It targets high accuracy, possibly using docling library, with a custom json `colomnHeader.json` defining the output schema and headers.


## ✨ Features

- **Invoice Data Extraction:** Processes invoice images or other data formats to extract relevant information.
- **Data Cleaning and Transformation:** Cleans and transforms extracted data to ensure accuracy and consistency.
- **Excel Output:** Generates a well-formatted CSV file (.csv) containing the extracted data.
- **Customizable Output:** (Likely) allows customization of output fields through configuration (needs confirmation via code review).
- **High Accuracy:** Aims for a high degree of accuracy in data extraction.

## Logical Overview
  <img src="https://github.com/user-attachments/assets/f3666700-6898-450d-85c9-fc4e101c71b8" alt="Second" style="width: 150%; height: 500px; object-fit: contain;"/>



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

The `colomnHeader.json` file defines the structure of the output Excel file.  Its contents and format should be documented.  (Analyze `colomnHeader.json` and describe its structure and the role of each key.)



---

<div align="center">

**Made with ❤️ by KrupalWarale**

</div>
