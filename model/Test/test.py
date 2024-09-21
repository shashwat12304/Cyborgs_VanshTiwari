# Importing the Keras OCR library
import keras_ocr
import matplotlib.pyplot as plt
import numpy as np

# keras-ocr will automatically download pretrained
# weights for the detector and recognizer.
pipeline = keras_ocr.pipeline.Pipeline()

# Get a set of two example images
images = [
    keras_ocr.tools.read(img) for img in [r'C:\Users\Shashwat.Sharma\Documents\cyborgs\VideoFrames\video1\frame_0.jpg']
]

# generate text predictions from the images
prediction_groups = pipeline.recognize(images)

# plot the text predictions
fig, axs = plt.subplots(nrows=len(images), figsize=(10, 20))
for ax, image, predictions in zip(axs, images, prediction_groups):
    keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)
    text = [text for text, box in predictions]
    ax.set_title(' '.join(text))# extracted text putting as title to the plot