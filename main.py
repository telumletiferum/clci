# Script that takes an image that conctains english, arabic and simplified chinese and displays the bounding boxes of the english text

import cv2
import pytesseract


def detect_english_characters(path_to_image):
    # Read image with opencv
    img = cv2.imread("" + path_to_image)

    # Convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform otsu threshold
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

    # Appplying dilation on the threshold image
    dilation = cv2.dilate(thresh, rect_kernel, iterations=1)

    # Finding contours
    contours = cv2.findContours(
        dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )

    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written to a variable and concatenated
    final_text = ""
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Cropping the text block for giving input to OCR
        cropped = img[y : y + h, x : x + w]

        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped, lang="eng+ara+chi_sim")

        # Store the text in a variable
        final_text = final_text + text

    # Count only english characters in the final text
    english_count = 0
    for char in final_text:
        if ord(char) >= 65 and ord(char) <= 122:
            english_count += 1
    print(english_count)


# Input the path to the image
print("Would you like to use default test image provided? (y/n)")
choice = input()
if choice == "y":
    detect_english_characters("test/data/test.png")
else:
    console_input = input("Enter the path to the image: ")
    detect_english_characters(console_input)
