# **Billwizard: ChatOCR**

## Overview

**Billwizard: ChatOCR** is a powerful desktop application designed to capture video input (via webcam or pre-recorded video) to detect and extract the total bill amount from invoices. The tool leverages **Optical Character Recognition (OCR)** using Tesseract and integrates machine learning algorithms to categorize the invoices based on their content. The extracted data can then be exported in formats like **CSV, JSON, or XML** for downstream analysis or storage.The integration of **RAG** over invoices gives the capability of analyzing invoices for tasks such as Anomaly Detection using Natural language.

---
<div align="center">
  <h2>Architecture Diagram</h2>
  <br>
  <img alt="snake eating my contributions" src="https://github.com/shashwat12304/shashwat12304/blob/main/Utils/DATSAW.drawio.png"/>
  <br/><br/><br/>
</div>
---
## Results Comparsion
`Results comparison of Vision LLMs with Traditional Approaches`: Results saved in FinalResults folder
Here’s a comparison between **Vision LLMs** (Large Language Models) and **traditional OCR approaches** like **PyTesseract** and **EasyOCR**, focusing on key factors such as accuracy, language support, generalization, flexibility, and more:


| **Criteria**               | **Vision LLMs** (e.g., Donut, TrOCR, GPT-4 Vision)          | **PyTesseract**                     | **EasyOCR**                          |
|----------------------------|------------------------------------------------------------|-------------------------------------|--------------------------------------|
| **OCR Accuracy**            | High accuracy, especially with complex, dense, or multi-lingual documents. Can handle unstructured and noisy data effectively. | Good for structured, clean documents but struggles with complex layouts or distorted images. | Better than PyTesseract for some fonts and languages but still struggles with highly complex documents. |
| **Multimodal Capabilities** | Can combine text extraction with contextual understanding and image reasoning, e.g., answering questions about images or extracting structured data from unstructured formats. | Limited to text extraction only. Cannot interpret images beyond identifying text regions. | Focuses on text extraction only, with no understanding of surrounding context or image content. |
| **Generalization**          | Generalizes well to unseen document types and structures thanks to pretraining on large, diverse datasets. | Requires pre-processing steps and struggles to generalize to unseen or complex document structures. | Slightly better generalization than PyTesseract but still limited compared to Vision LLMs. |
| **Language Support**        | Supports a wide range of languages due to large-scale pretraining (can handle multiple scripts and even complex or low-resource languages). | Strong support for 100+ languages but accuracy may vary, especially with lesser-known or non-standard languages. | Supports 80+ languages, often better with East Asian scripts, but might lag in rare language or complex scripts. |
| **Complex Layout Handling** | Excels in handling complex layouts, tables, charts, and dynamic visual elements within documents. | Requires manual specification or segmentation of regions for accurate text extraction from complex layouts. | Can handle more layouts than PyTesseract but still not as efficient with highly structured documents (e.g., invoices, forms). |
| **Model Customization**     | Pretrained Vision LLMs can be fine-tuned for specific use cases or document types, improving performance for specialized tasks. | Limited scope for customization beyond changing pre-processing or post-processing steps. | Allows some tuning with specific parameters but lacks the flexibility of training for custom use cases. |
| **Speed**                   | Slower than traditional OCR methods due to larger model size and computational overhead, but modern models are optimized to work faster on specialized hardware (TPUs, GPUs). | Very fast, lightweight, works efficiently on CPU. | Reasonably fast, especially when using GPU, but slower than PyTesseract on CPU. |
| **Contextual Understanding**| Vision LLMs can "understand" and interpret the context around the text (e.g., image reasoning or content comprehension). They can process both visual and semantic context. | No contextual understanding, limited to raw text extraction. | Limited to pure OCR with no contextual understanding. |
| **Flexibility**             | Highly flexible, can be used for diverse tasks like document parsing, visual question answering, and content generation from images. | Best for basic OCR tasks, not suitable for complex or dynamic use cases. | Offers flexibility in terms of language but remains limited to text extraction. |
| **Pre-processing Requirement** | Minimal pre-processing required, thanks to strong generalization capabilities. | Requires significant pre-processing (e.g., thresholding, noise removal) for optimal accuracy. | Requires less pre-processing than PyTesseract, but still needed for challenging cases. |
| **Deployment Complexity**   | Requires specialized hardware (GPU/TPU) for optimal performance, and can be more complex to deploy than traditional OCR solutions. | Easy to deploy on a wide range of systems, including low-power devices; requires minimal dependencies. | Similar to PyTesseract in terms of deployment simplicity but may benefit more from GPU. |
| **Cost**                    | Expensive to run due to high computational power, especially for large-scale or real-time applications. | Very cost-effective, minimal compute resources required. | Moderate resource usage, cheaper than Vision LLMs but more resource-hungry than PyTesseract. |
| **Use Case Examples**       | Complex document processing (invoices, legal documents), visual question answering, generating structured data from unstructured images. | Simple document OCR (scanned documents, printed text), bulk text extraction. | Multi-language OCR, better suited for simpler documents, handwritten text, and East Asian scripts. |
---
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
