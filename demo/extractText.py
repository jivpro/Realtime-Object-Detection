from PIL import Image
from pytesseract import image_to_string
import sys

img=Image.open(sys.argv[1])
text=image_to_string(img,lang='eng')
print(text)