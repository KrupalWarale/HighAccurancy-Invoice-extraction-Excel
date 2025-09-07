# HighAccuracy Invoice Extraction to Excel

A comprehensive tool designed to automate the extraction of data from PDF invoices, transforming them into structured, Excel-compatible CSV files with high accuracy. This project addresses the common challenge of manually processing invoices by providing an intelligent, configurable system that handles various invoice formats and layouts.

## Overview

In today's fast-paced business environment, processing invoices manually can be time-consuming and error-prone. This project offers a solution by automatically extracting key information from PDF invoices, including both tabular data (like item details, quantities, and prices) and unstructured metadata (such as invoice numbers, dates, and vendor information). It employs advanced techniques like fuzzy string matching for header normalization, ensuring that even invoices with slight variations in formatting are processed correctly.

The system is built to be flexible and scalable, making it suitable for small businesses as well as larger enterprises dealing with high volumes of invoices. It organizes processed files systematically, tracks successes and failures, and provides clear outputs that can be easily imported into Excel or other data analysis tools.

## Key Features

- **Intelligent Data Extraction**: The tool extracts both structured tabular data and unstructured metadata from PDF invoices, handling complex layouts with nested tables and multi-page documents.
- **Header Normalization**: Uses a configurable dictionary of synonyms to map invoice headers to standardized formats, accommodating variations in naming conventions across different vendors.
- **Multi-Table Merging**: Intelligently combines data from multiple tables within a single invoice, using unique identifiers to maintain data integrity.
- **Robust Error Handling**: Automatically categorizes processing attempts as successful or failed, with detailed logging for troubleshooting.
- **Flexible Output Formats**: Generates CSV files for tabular data (ready for Excel import) and JSON files for metadata, providing comprehensive information extraction.
- **Unique Identification**: Assigns unique invoice numbers and hashes for traceability and to prevent duplicate processing.
- **Configurable Processing**: Allows customization of extraction rules through a JSON configuration file, adapting to specific business needs.

## Installation

Before installing, ensure you have Python 3.8 or higher installed on your system. You can download Python from the official website if needed.

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/your-username/highaccuracy-invoice-extraction.git
   cd highaccuracy-invoice-extraction
   ```

2. Install the required Python packages:
   ```
   pip install pandas docling
   ```

   Note: The `docling` library handles PDF processing, while `pandas` is used for data manipulation and CSV generation.

## Usage

Using the tool is straightforward. Here's a step-by-step guide:

1. **Prepare Your Invoices**: Place all PDF invoices you want to process in the `input/` directory. The tool will automatically detect and process all PDF files in this folder.

2. **Configure Header Mappings** (Optional): If your invoices use non-standard header names, edit the `colomnHeader.json` file to add synonyms for better recognition. This step is crucial for achieving high accuracy in data extraction.

3. **Run the Extraction**: Execute the main script from the command line:
   ```
   python main.py
   ```

4. **Monitor Progress**: The script will process each PDF file, displaying progress messages in the console. Successfully processed files are moved to `processed/success/`, while failed ones go to `processed/failed/`.

5. **Access Results**: 
   - Tabular data will be appended to `output/output.csv`, ready for import into Excel or other spreadsheet applications.
   - Metadata for each invoice is saved as individual JSON files in `output/json/`, named by the invoice's unique hash.

6. **Review and Verify**: Open the CSV file in Excel to verify the extracted data. Check the JSON files for any additional metadata that might be useful.

## Configuration

The `colomnHeader.json` file is central to the tool's accuracy. It contains mappings of standard field names to their possible variations in invoices. Here's an example structure:

```json
{
  "unique_identifiers": ["hsn_sac_identifier", "item_code"],
  "invoice_details": {
    "Invoice Number": ["invoice_no", "inv_no", "bill_no", "invoice_number"],
    "Date": ["date", "invoice_date", "bill_date", "issue_date"],
    "Vendor Name": ["vendor", "supplier", "seller", "company"]
  },
  "item_details": {
    "Description": ["item", "product", "description", "particulars"],
    "Quantity": ["qty", "quantity", "amount"],
    "Unit Price": ["rate", "price", "unit_price"],
    "Total": ["total", "amount", "line_total"]
  }
}
```

To customize:
- Add new sections for different types of data you want to extract.
- Include as many synonyms as possible for each field to improve matching accuracy.
- The `unique_identifiers` array specifies fields that can be used to merge data from multiple tables.

## Project Structure

Understanding the project layout helps in troubleshooting and customization:

- `input/`: Drop your PDF invoices here for processing
- `processed/success/`: PDFs that were successfully processed and extracted
- `processed/failed/`: PDFs that couldn't be processed (check console logs for reasons)
- `output/output.csv`: The main output file containing all extracted tabular data
- `output/json/`: Directory containing JSON files with metadata for each invoice
- `colomnHeader.json`: Configuration file for header mappings and synonyms
- `main.py`: The main Python script that orchestrates the entire extraction process

## How It Works

The extraction process involves several steps:

1. **PDF Parsing**: Uses the Docling library to convert PDF content into a structured format.
2. **Metadata Extraction**: Scans the text content for key-value pairs, handling multi-line values and context.
3. **Table Detection**: Identifies and extracts tabular data from the PDF.
4. **Header Normalization**: Applies fuzzy matching to map detected headers to standard names using the synonym dictionary.
5. **Data Merging**: Combines multiple tables using unique identifiers, ensuring data consistency.
6. **Output Generation**: Creates CSV and JSON outputs, assigns unique identifiers, and organizes files.

## Troubleshooting

If you encounter issues:

- **Low Accuracy**: Review and expand the synonyms in `colomnHeader.json`.
- **Processing Failures**: Check the console output for specific error messages. Common issues include corrupted PDFs or unsupported layouts.
- **Missing Data**: Ensure your invoices follow a consistent format. The tool works best with structured invoices.
- **Performance Issues**: For large volumes, consider processing in batches or optimizing the synonym dictionary.

## Technologies Used

- **Python**: The core programming language, chosen for its extensive libraries and ease of use.
- **Pandas**: Powerful data manipulation library for handling CSV operations and dataframes.
- **Docling**: Specialized library for converting PDF documents to structured data.
- **Difflib**: Standard library module for fuzzy string matching and header normalization.

## Contributing

We welcome contributions to improve the tool's accuracy and functionality. Here's how you can help:

1. Fork the repository on GitHub.
2. Create a feature branch for your changes.
3. Make your modifications, ensuring they include appropriate tests.
4. Submit a pull request with a clear description of your changes.

Please report any bugs or suggest features by opening issues on the GitHub repository.

## License

This project is licensed under the MIT License, which allows for free use, modification, and distribution. See the LICENSE file for full details.

## Future Enhancements

We're continuously working to improve the tool. Planned features include:
- Support for additional output formats (e.g., Excel .xlsx files)
- Machine learning-based header recognition for even better accuracy
- Web-based interface for easier configuration and monitoring
- Integration with popular accounting software

If you have suggestions for improvements, please let us know through the GitHub issues.
