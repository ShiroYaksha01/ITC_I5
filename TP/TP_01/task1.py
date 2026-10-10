# Task1: Create color images
# Now that your environment is ready, let's the test with a simple challenge using OpenCV.
# Create 3 images, each represents Red image, Green image, and Blue image with 500pixels Height and 300pixels Width.

import cv2
import numpy as np

height=500
width=300

# create 3 blank images
red_image=np.zeros((height,width,3), dtype=np.uint8)
blue_image=np.zeros((height,width,3), dtype=np.uint8)
green_image=np.zeros((height,width,3), dtype=np.uint8)

# set colors
red_image[:,:]=[0,0,255]
blue_image[:,:]=[0,255,0]
green_image[:,:]=[255,0,0]

# create 3 images
cv2.imwrite('images/red_image.jpg', red_image)
cv2.imwrite('images/blue_image.jpg', blue_image)
cv2.imwrite('images/green_image.jpg', green_image)

# Show images
cv2.imshow('Red Image', red_image)
cv2.imshow('Blue Image', blue_image)
cv2.imshow('Green Image', green_image)

print("Press any key in an image window to close.")

# Wait for key press and clean up
cv2.waitKey(0)
cv2.destroyAllWindows()