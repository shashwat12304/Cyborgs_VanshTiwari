from doctr.io import DocumentFile
from doctr.models import ocr_predictor
model = ocr_predictor(pretrained=True)
single_img_doc = DocumentFile.from_images(r"C:\Users\Shashwat.Sharma\Documents\cyborgs\VideoFrames\video1\frame_0.jpg")
result = model(single_img_doc)