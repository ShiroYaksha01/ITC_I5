# Task2: Draw Rectangle and Diagonal
# Create a blank image, then draw a rectangle and diagonal of the image
# DO NOT USE build-in: e.g. cv2.line(), cv2.rectangle()

import cv2
import numpy as np

win_height=650
win_width=500

rect_height=150
rect_width=250

rect_starting_pos=100

# creating blank image
image=np.zeros((win_height,win_width, 3), dtype=np.uint8)

# Drawing green rectangle
image[rect_starting_pos:rect_starting_pos+rect_height, rect_starting_pos:rect_starting_pos+rect_width]=[0,255,0]

# Drawing blue diagonal line
for x in range(win_width):
    y = int(x * (win_height - 1) / (win_width - 1))
    image[y, x] = [255, 0, 0]


# showing the image
cv2.imshow("Rectangle and Diagonal", image)
print("Press any key in an image window to close.")

# Wait for key press and clean up
cv2.waitKey(0)
cv2.destroyAllWindows()