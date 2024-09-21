# **Billwizard: ChatOCR**

## Overview

**Billwizard: ChatOCR** is a powerful desktop application designed to capture video input (via webcam or pre-recorded video) to detect and extract the total bill amount from invoices. The tool leverages **Optical Character Recognition (OCR)** using Tesseract and integrates machine learning algorithms to categorize the invoices based on their content. The extracted data can then be exported in formats like **CSV, JSON, or XML** for downstream analysis or storage.

---
<div align="center">
  <h2>Architecture Diagram</h2>
  <br>
  <img alt="snake eating my contributions" src="https://github.com/shashwat12304/shashwat12304/blob/main/Utils/DATSAW.drawio.png"/>
  <br/><br/><br/>
</div>

## Key Features

1. **Video Input Capture**: 
   - Capture invoice data via live webcam input or pre-recorded video files for real-time or near-real-time analysis.
   
2. **OCR for Bill Amount Detection**: 
   - Use **Tesseract OCR** to extract text and identify the total bill amount from invoices.
   
3. **Invoice Categorization**:
   - Employ machine learning models (e.g., Logistic Regression, SVM) to classify invoices into predefined categories such as **groceries, electronics, and services** based on the extracted text.

4. **Data Export**: 
   - Export detected bill amounts and categorized data in structured formats like **CSV, JSON, or XML** for downstream use or storage.

---

## Tech Stack

### Programming Language:
- **Python**

### Libraries and Dependencies:
1. **OpenCV** (`opencv-python`): For capturing video input, extracting frames, and analyzing images.
2. **Tesseract OCR** (`pytesseract`): For extracting textual information from invoice images.
3. **Gradio** (`gradio`): Provides a web-based interface to interact with the application.
4. **Pandas** (`pandas`): For data manipulation, including handling invoice data in tabular format for conversions.
5. **ChromaDB** (`chromadb`): A vector database used in the **Retrieval-Augmented Generation (RAG)** system.
6. **Ollama** (`Ollama`): For using Open source LLM
7. **Langchain** (`langchain`): For RAG over Bill invoices

---

## Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/Billwizard-ChatOCR.git
cd Billwizard-ChatOCR
```

### Step 2: Set up a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate     # On macOS/Linux
# venv\Scripts\activate      # On Windows

pip install -r requirements.txt
```

### Step 3: Download and install Tesseract OCR
- [Tesseract OCR Installation Instructions](https://github.com/tesseract-ocr/tesseract)

### Step 4: Run the application
```bash
python Scripts/integration.py
```

---

## Project Structure

Here is a breakdown of the project’s folder structure and the purpose of each component:

```bash
Billwizard-ChatOCR/
│
├── converters/                # Handles file conversions (JSON ↔ Excel)
│   ├── jsontoxls.py            # Converts JSON files to Excel
│   └── xlstojson.py            # Converts Excel files to JSON
│
├── DATSAW/                    # Placeholder for future data analysis/scraping
│
├── DB/                        # Placeholder for database configurations
│
├── Scripts/                   # Main scripts for processing
│   ├── integration.py          # Orchestrates video/image processing, OCR, and Gradio UI
│   ├── processor.py            # Handles video-to-image conversion and OCR
│   └── rag.py                  # Implements the RAG (Retrieval-Augmented Generation) system
│
├── Utils/                     # Utility scripts
│   └── camera.py               # Captures real-time images using the system’s webcam
│
├── VideoFrames/               # Contains extracted frames from video files
│
├── requirements.txt           # List of dependencies
└── README.md                  # Project documentation
```

### Detailed Breakdown

1. **converters/**: 
   - This folder contains utilities for converting data between JSON and Excel formats.
   - **jsontoxls.py**: Converts a JSON file into an Excel file using `pandas`.
   - **xlstojson.py**: Converts an Excel file into JSON format using `pandas` and `excel2json`.

2. **DATSAW/**: 
   - Placeholder for future data analysis or scraping functionality.
   - This folder may be extended in the future for more advanced data handling operations.

3. **DB/**: 
   - Placeholder for any future database integration or configuration.
   - In future versions, this can be used to store invoice data persistently.

4. **Scripts/**:
   - **integration.py**:
     - The main orchestrator script that integrates video/image processing, OCR, and user interface using **Gradio**.
     - Allows users to upload invoices or capture images, runs OCR on them, and categorizes them.
   - **processor.py**:
     - Handles the actual video-to-image conversion using OpenCV.
     - Also manages text extraction via **Tesseract OCR** and calls relevant functions for processing images.
   - **rag.py**:
     - Implements the **Retrieval-Augmented Generation (RAG)** system for querying and retrieving invoice-related data using **ChromaDB**.

5. **Utils/**:
   - **camera.py**:
     - Utility for capturing real-time images from the system’s webcam.
     - Stores captured images with a timestamp for easy tracking.

6. **VideoFrames/**:
   - Stores frames extracted from video files during processing.
   - These frames are then passed into the OCR system for text extraction.

7. **requirements.txt**: 
   - Contains a list of Python libraries and dependencies required to run the application, including **OpenCV**, **Tesseract**, **Gradio**, **Scikit-learn**, etc.

---

## Usage

### Step 1: Launch the Gradio Interface

Run the following command to launch the Gradio web app for interacting with the system:
```bash
python Scripts/integration.py
```

### Step 2: Interact with the Interface

- Upload a pre-recorded video or use your webcam to capture an invoice.
- The system will extract relevant details such as the **total bill amount** using Tesseract OCR.
- The system will categorize the invoice based on its content (e.g., groceries, electronics, services).

### Step 3: Export Data

Once processed, export the extracted invoice data in **CSV**, **JSON**, or **XML** formats for downstream processing or storage.

---

## Error Handling

| **Error**                           | **Reason**                                                 | **Solution**                                                                                     |
|-------------------------------------|------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| `FileNotFoundError`                 | Tesseract is not installed or misconfigured.                | Ensure Tesseract is installed correctly and the path is properly configured in your environment.  |
| `ModuleNotFoundError: No module`    | Required dependencies (e.g., `opencv-python`) are missing.  | Run `pip install -r requirements.txt` to install missing libraries.                              |
| `cv2.error`                         | Issues with reading or processing a video file.             | Ensure the video format is supported by OpenCV and that the file is not corrupted.                |
| `pandas.errors.EmptyDataError`      | The file for conversion is empty or invalid.                | Check that the input files are correctly formatted and contain valid data before running scripts. |
| `ValueError: Invalid collection`    | Trying to access a non-existent collection in ChromaDB.     | Ensure the collection exists before trying to retrieve or add data to it.                        |

---

## Future Enhancements

1. **Improve User Privacy and Security**
2. **Implement DATSAW**
3. **Multi-language Support**
4. **Implement Vision Agents**
5. **Implement Tree Organized Analysis algorihms such as `RAPTOR`**
