import os
import cv2

image = cv2.imread(os.path.join('.','tigerII.jpg'))
image = cv2.resize(image, (750, 400))
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #Blue green red to red green blue
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Blue green red to gray
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #Blue green red to HSV
cv2.imshow('HSV TIGER II',hsv_image)
cv2.imshow('RGB TIGER II',rgb_image)
cv2.imshow('GRAY TIGER II', gray_image)
cv2.imshow('TIGER II',image)
cv2.waitKey(0)