from google.cloud import vision
import io

# Initialize Google Cloud Vision API client
client = vision.ImageAnnotatorClient()

# Load the image file
with io.open(r'C:\Users\Shashwat.Sharma\Documents\cyborgs\VideoFrames\video1\frame_0.jpg', 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Perform OCR on the image
response = client.text_detection(image=image)
texts = response.text_annotations

# Print extracted text
for text in texts:
    print(text.description)
