# Program that takes an image containing text in english, arabic and chinese but displays only the bounding boxes of the text in english

import cv2
import numpy as np
import pytesseract

# Read image with opencv
img = cv2.imread("test/data/test.png")

# Convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply dilation and erosion to remove some noise
kernel = np.ones((1, 1), np.uint8)
gray = cv2.dilate(gray, kernel, iterations=1)
gray = cv2.erode(gray, kernel, iterations=1)

# Write image after removed noise
# cv2.imwrite("removed_noise.png", gray)

# Apply threshold to get image with only black and white
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Write the image after apply opencv to do some ...
# cv2.imwrite("thres.png", gray)

# Recognize text with tesseract for python
result = pytesseract.image_to_string(gray, lang="eng")

# Remove template file
# os.remove(temp)

# Print recognized text
print(result)

# Create a list of all the bounding boxes whitelisting the characters we want
boxes = pytesseract.image_to_boxes(
    img,
    lang="eng",
    config="--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
)  # also try specifying "chi_sim" or "ara" for chinese and arabic

# Loop through all the bounding boxes
for b in boxes.splitlines():
    # Split the bounding box into x, y, width, height
    b = b.split(" ")
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    # Draw the bounding box
    cv2.rectangle(img, (x, img.shape[0] - y), (w, img.shape[0] - h), (0, 255, 0), 1)

# Show the image with the bounding box
cv2.imshow("img", img)
cv2.waitKey(0)
