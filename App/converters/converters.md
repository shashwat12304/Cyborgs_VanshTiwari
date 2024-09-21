# **Converters Module Documentation**

## Overview

The **Converters** folder contains scripts designed to handle the conversion between JSON and Excel formats. These converters simplify the process of transforming data structures, making it easier to switch between formats for various applications such as data analytics, reporting, and data exchange.

---

## Files in the Converters Folder

### 1. **`jsontoxls.py`**
   - **Purpose**: 
     - This script converts JSON files into Excel files. It is useful when you need to move structured data stored in JSON format into a tabular form for easier analysis, reporting, or sharing.
     
   - **Key Components**:
     - **Class `JsonToExcelConverter`**:
       - This class is designed to convert JSON data into an Excel spreadsheet using the **`pandas`** library.
       - **Methods**:
         - **`__init__(self, input_json_file: str, output_excel_file: str)`**:
           - Initializes the converter with the paths of the input JSON file and the output Excel file.
           - Parameters:
             - `input_json_file`: Path to the input JSON file.
             - `output_excel_file`: Path to the output Excel file.
         - **`convert(self)`**:
           - Reads the JSON file, converts it to a **`pandas` DataFrame**, and then writes the DataFrame to an Excel file. This method automatically handles the parsing of JSON into tabular format, making sure that the data is written correctly into Excel.

   - **Usage Example**:
     ```python
     from jsontoxls import JsonToExcelConverter
     
     converter = JsonToExcelConverter("input_data.json", "output_data.xlsx")
     converter.convert()
     ```
   
   - **Dependencies**:
     - **`pandas`**: Used for handling data in tabular form and converting it to an Excel spreadsheet.

---

### 2. **`xlstojson.py`**
   - **Purpose**: 
     - This script converts Excel files into JSON format. It is designed to handle cases where tabular data in Excel needs to be programmatically processed in JSON form for integration with APIs, applications, or other systems.
     
   - **Key Components**:
     - **Class `ExcelToJsonConverter`**:
       - Converts an Excel spreadsheet into a JSON file using **`pandas`** and **`excel2json`** libraries.
       - **Methods**:
         - **`__init__(self, input_excel_file: str, output_json_file: str, sheet_name: str = 'sheet1', engine: str = None)`**:
           - Initializes the converter with the paths to the input Excel file, the output JSON file, and an optional sheet name.
           - Parameters:
             - `input_excel_file`: Path to the input Excel file.
             - `output_json_file`: Path to the output JSON file.
             - `sheet_name`: The name of the sheet to convert (default is `'sheet1'`).
             - `engine`: Specifies the parsing engine if needed (optional).
         - **`convert(self)`**:
           - Reads the Excel file into a **`pandas` DataFrame**, then converts the DataFrame to a JSON structure and writes it to a file. This method handles parsing of tabular data from Excel, transforming it into JSON format for further use.

   - **Usage Example**:
     ```python
     from xlstojson import ExcelToJsonConverter
     
     converter = ExcelToJsonConverter("input_data.xlsx", "output_data.json")
     converter.convert()
     ```

   - **Dependencies**:
     - **`pandas`**: Used for handling tabular data and converting it into JSON format.
     - **`excel2json`**: Additional helper library for parsing Excel files.

---

## Tech Stack

- **Python**: The main programming language for this module.
- **pandas**: A powerful data manipulation library for handling structured data.
- **excel2json**: A library used for converting Excel spreadsheets into JSON format.

---

## Control Flow and Interactions

The converters operate in isolation, converting data from one format to another. Control flow is straightforward:
- A user initializes the respective converter class (`JsonToExcelConverter` or `ExcelToJsonConverter`) with the appropriate input and output file paths.
- The `convert()` method is called to perform the conversion.
- The script reads data from the input format (JSON or Excel), processes it using `pandas`, and writes it to the output format.

---

## Common Errors, Reasons, and Solutions

| **Error**                  | **Reason**                                                                                     | **Solution**                                                                                      |
|----------------------------|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| `FileNotFoundError`         | The input file path provided doesn't exist or is incorrect.                                    | Ensure the file paths for both input and output files are correct.                                 |
| `ValueError: Invalid file`  | The input file is not a valid JSON or Excel file.                                               | Verify that the input file has the correct format (e.g., `.json` for JSON, `.xlsx` for Excel).     |
| `pandas.errors.EmptyDataError` | The file is empty or contains no data.                                                       | Check that the input file contains valid data before attempting to convert it.                     |
| `ModuleNotFoundError: No module named 'pandas'` | The required `pandas` or `excel2json` modules are not installed.                      | Install the missing dependencies using `pip install pandas excel2json`.                           |
| `UnicodeDecodeError`        | Issues with file encoding, especially for non-UTF8 encoded files.                             | Ensure the file encoding is UTF-8 or specify the correct encoding when reading the file.           |

---

## Installation

To install the necessary dependencies for this module, create a virtual environment and install the required libraries:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. Install the required libraries:
   ```bash
   pip install -r requirements_converters.txt
   ```

---

## Summary

The **Converters** module provides a simple and effective way to convert between JSON and Excel formats. With two main scripts—`jsontoxls.py` and `xlstojson.py`—this module can easily be integrated into any data pipeline or used independently for conversion tasks. The use of `pandas` ensures robust data handling, and the addition of `excel2json` simplifies Excel-to-JSON conversion, making the scripts easy to use for both developers and non-developers.

---