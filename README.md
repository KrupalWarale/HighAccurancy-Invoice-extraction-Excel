# HighAccuracy Invoice Extraction to Excel

A robust tool for extracting data from PDF invoices and converting it into structured Excel-compatible CSV files with high accuracy.

## Overview

This project automates the process of extracting key information from PDF invoices, including tabular data and metadata. It uses intelligent header normalization to map invoice fields to standardized formats, handles multiple tables, and organizes processed files efficiently.

## Key Features

- **Accurate Data Extraction**: Extracts both structured tables and unstructured metadata from PDF invoices
- **Header Normalization**: Maps invoice headers to standard formats using a configurable synonym dictionary
- **Multi-Table Handling**: Merges data from multiple tables within a single invoice
- **Error Handling**: Automatically categorizes successful and failed processing attempts
- **Output Formats**: Generates CSV files for tabular data and JSON files for metadata

## Installation

1. Ensure you have Python 3.8 or higher installed.
2. Install the required dependencies:
   ```
   pip install pandas docling
   ```

## Usage

1. Place your PDF invoices in the `input/` directory.
2. Configure the header mappings in `colomnHeader.json` if needed.
3. Run the main script:
   ```
   python main.py
   ```
4. Processed data will be available in `output/output.csv` and `output/json/`.
5. Check the `processed/success/` and `processed/failed/` directories for file status.

## Configuration

Edit `colomnHeader.json` to customize header mappings:

```json
{
  "unique_identifiers": ["hsn_sac_identifier"],
  "invoice_details": {
    "Invoice Number": ["invoice_no", "inv_no", "bill_no"],
    "Date": ["date", "invoice_date", "bill_date"]
  }
}
```

## Project Structure

- `input/`: Directory for PDF invoices to be processed
- `processed/success/`: Successfully processed PDFs
- `processed/failed/`: PDFs that failed processing
- `output/output.csv`: Extracted tabular data
- `output/json/`: Metadata in JSON format
- `colomnHeader.json`: Configuration for header mappings
- `main.py`: Main processing script

## Technologies

- Python
- Pandas for data manipulation
- Docling for PDF processing
- Difflib for fuzzy string matching

## Contributing

Feel free to submit issues or pull requests for improvements.

## License

This project is licensed under the MIT License.
