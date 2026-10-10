# Task5: Convert Grayscale to binary image
# Load an image as RGB, covert it to Grayscale and then covert to binary image using your own Threshold.
# DO NOT USE build-in: e.g. cv2.cvtColor(), cv2.threshold()

import cv2
import numpy as np

# Load image
image = cv2.imread("images/test.jpeg")

if image is None:
    print("Error: Could not load image.")
    exit()

# Get BGR channels
blue = image[:, :, 0]
green = image[:, :, 1]
red = image[:, :, 2]

# Convert to grayscale
grayscale = (
    0.114 * blue +
    0.587 * green +
    0.299 * red
)

# Convert to binary image using a threshold from grayscale
threshold = 125
binary_image = np.where(grayscale >= threshold, 255, 0).astype(np.uint8)

# Convert back to 8-bit pixel values
grayscale = grayscale.astype(np.uint8)

# Show images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale", grayscale)
cv2.imshow("Binary Image", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()