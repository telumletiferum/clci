# Program that counts all latin letters in an image that also contains arabic letters and chinese letters
from PIL import Image
import pytesseract

# Read image
img = Image.open("test/data/image.png")

# Convert image to string
text = pytesseract.image_to_string(img)
print(text)
