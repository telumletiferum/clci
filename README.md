# CLCI (count latin characters in image)

This is a simple python project that implements Google's tesseract-ocr in order to count the latin characters from a given image that also has arabic and/or chinese characters.

# Requirements

This script utilizes pytesseract as such you must have Tesseract OCR installed on system. This script also assumes that you have Tesseract added to your PATH. For more info check [Tesseract documentation](https://tesseract-ocr.github.io/tessdoc/Installation.html). If you don't have it added to PATH for some or other reasons you need to add this line of code to main.py

`pytesseract.pytesseract.tesseract_cmd = 'System_path_to_tesseract.exe'`

pip dependencies can be installed via

`pip install -r requirements.txt`

Creating a python virtual environment is recommended

# Caveats and limitations

Results obtained running this script are really dependent on source image that you are using. The script in it's current version works really well with document-like text as seen with the test images. Technically it should work with images that are a bit more complex however your results might vary very much from case to case. Unfortunately that's just the reality of using OCR technology.
