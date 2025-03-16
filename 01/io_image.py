import os
import cv2

# read image
image_path = os.path.join('.','data','tank.jpg')
img = cv2.imread(image_path)

#write image
cv2.imwrite(os.path.join('.','data','tank_out.jpg'), img)

#visualize image
cv2.imshow('name of window', img)
cv2.waitKey(0)