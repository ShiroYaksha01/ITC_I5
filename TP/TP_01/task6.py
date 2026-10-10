# Task6: Flip image
# Load an image as RGB, then flip it vertical and horizontal.
# DO NOT USE build-in: e.g. cv2.flip()

import cv2

# Load image
image = cv2.imread("images/test.jpeg")

if image is None:
    print("Error: Could not load image.")
    exit()

# Vertical flip
vertical = image[::-1, :, :]

# Horizontal flip
horizontal = image[:, ::-1, :]

# Show results
cv2.imshow("Original Image", image)
cv2.imshow("Vertical", vertical)
cv2.imshow("Horizontal", horizontal)

cv2.waitKey(0)
cv2.destroyAllWindows()