
<img width="1919" height="626" alt="doc" src="https://github.com/user-attachments/assets/22ea60f3-3c74-44ea-8b89-75f19d34e588" />


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

## Logical Overview


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
