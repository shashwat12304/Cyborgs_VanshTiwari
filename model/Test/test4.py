from transformers import DonutProcessor, VisionEncoderDecoderModel
from PIL import Image

# Load Donut pre-trained model from Hugging Face
processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base")
model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base")

# Load and preprocess image
image = Image.open(r"C:\Users\Shashwat.Sharma\Documents\cyborgs\VideoFrames\video1\frame_0.jpg")
pixel_values = processor(image, return_tensors="pt").pixel_values

# Perform inference
generated_text = model.generate(pixel_values)

# Decode and print the extracted text
result = processor.decode(generated_text[0])
print(result)
