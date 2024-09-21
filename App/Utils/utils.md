# **Utils Module Documentation**

## Overview

The **Utils** folder contains utility scripts that provide additional functionalities to the main application. These utilities are designed to perform specific tasks that enhance the app's core functionality, such as capturing images from a webcam.

---

## Files in the Utils Folder

### 1. **`camera.py`**
   - **Purpose**:
     - This script is designed to capture images from the system’s webcam and save them to a designated folder. It’s useful for real-time image capture, which can be further processed for other tasks such as video frame analysis, object detection, or data gathering.
   
   - **Key Components**:
     - **Function `capture_and_save_image()`**:
       - Captures an image using the system's default camera and saves the image with a timestamped filename.
       - **Process Flow**:
         1. **Camera Initialization**: 
            - The script uses **OpenCV (`cv2`)** to access the default webcam (camera index `0`).
            - If the camera cannot be opened, an error message is printed.
         2. **Frame Capture**: 
            - The camera captures a single frame, and if it fails to do so, the camera is released, and an error message is printed.
         3. **Saving the Image**:
            - Captured images are saved in a folder named `captured_images`. If the folder does not exist, it is created.
            - The image file is named based on the current timestamp (`YYYYMMDD_HHMMSS.jpg`), ensuring each captured image has a unique filename.
       - **Use Case**:
         - This script can be used for applications that require real-time image data collection or monitoring, like surveillance systems or image-based processing pipelines.
   
   - **Usage Example**:
     ```python
     from camera import capture_and_save_image
     
     capture_and_save_image()
     ```

   - **Dependencies**:
     - **OpenCV (`cv2`)**: This library is crucial for handling real-time image and video capture from the system’s webcam.
     - **`os`**: Used to handle file and directory operations, such as checking for the existence of the `captured_images` directory and creating it if necessary.
     - **`datetime`**: Used to generate a timestamp for naming the captured images in a unique way.

---

## Tech Stack

- **Python**: The primary programming language.
- **OpenCV (`cv2`)**: A popular computer vision library for image and video processing tasks.

---

## Control Flow

The script `camera.py` performs a sequence of operations:
1. **Initialization**: The script attempts to open the system's default camera (camera index `0`).
2. **Frame Capture**: A single image frame is captured.
3. **Saving the Image**: The captured image is saved in the `captured_images` directory with a timestamp in its filename.

This utility can be integrated into other parts of the application for collecting real-time images, especially for tasks requiring image input from the user or real-time monitoring.

---

## Common Errors, Reasons, and Solutions

| **Error**                      | **Reason**                                              | **Solution**                                                                                       |
|---------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `Error: Could not open camera.` | The system’s webcam could not be accessed or is in use.  | Ensure that the camera is connected and not being used by other applications.                       |
| `Error: Could not capture image.`| The camera failed to capture a frame.                   | Make sure the camera is functional and that OpenCV is correctly installed and configured.            |
| `cv2.error`                     | Issues with OpenCV's interaction with the camera.        | Verify that OpenCV is properly installed. Check if your system’s webcam drivers are up to date.      |
| `PermissionError`               | Insufficient permissions to write files to the directory.| Ensure the script has write permissions for the folder where images are being saved.                |

---

## Installation

To ensure that the required dependencies are installed, create a virtual environment and install the necessary libraries:

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
   pip install opencv-python
   ```

---

## Summary

The **Utils** folder contains helper scripts, and `camera.py` provides the functionality to capture real-time images from the system’s webcam. This utility script can be seamlessly integrated into applications where real-time image capture is required. OpenCV simplifies the interaction with the camera, and `os` and `datetime` are used to manage the files and directories where images are saved.
