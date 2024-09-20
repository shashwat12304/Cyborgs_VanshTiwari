import cv2
import os
from datetime import datetime
def capture_and_save_image():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not capture image.")
        cap.release()
        return
    folder_name = "captured_images"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{folder_name}/capture_{timestamp}.jpg"
    cv2.imwrite(filename, frame)
    print(f"Image saved as {filename}")
    cap.release()

if __name__ == "__main__":
    capture_and_save_image()