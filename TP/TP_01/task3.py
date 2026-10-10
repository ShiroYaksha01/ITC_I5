# Task3: Split Image Channels
# Load an image as RGB, then split it to 3 images represent Red, Green, and Blue, respectively.
# DO NOT USE build-in: e.g. cv2.split()

import cv2
import numpy as np

# Load image
image = cv2.imread("images/test.jpeg")
# Fall back if the image is not found
if image is None:
    print("Error: Could not load image.")
    exit()

# Create blank images
red_image = np.zeros_like(image)
green_image = np.zeros_like(image)
blue_image = np.zeros_like(image)

# Split channels
blue_image[:, :, 0] = image[:, :, 0]
green_image[:, :, 1] = image[:, :, 1]
red_image[:, :, 2] = image[:, :, 2]

# Write images
cv2.imwrite('images/red_test_image.jpg', red_image)
cv2.imwrite('images/blue_test_image.jpg', blue_image)
cv2.imwrite('images/green_test_image.jpg', green_image)

# Show images
cv2.imshow("Original Image", image)
cv2.imshow("Red Image", red_image)
cv2.imshow("Green Image", green_image)
cv2.imshow("Blue Image", blue_image)

cv2.waitKey(0)
cv2.destroyAllWindows()