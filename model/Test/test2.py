import easyocr
reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
output =reader.readtext(r'C:\Users\Shashwat.Sharma\Documents\cyborgs\VideoFrames\video1\frame_0.jpg', detail = 0)
print(output)