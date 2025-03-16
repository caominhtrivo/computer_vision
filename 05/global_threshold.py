import os
import cv2

image = cv2.imread(os.path.join('.','bear.jpg'))
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray_image, 80, 255, cv2.THRESH_BINARY)
thresh = cv2.blur(thresh, (5,5))
ret, thresh = cv2.threshold(thresh, 80, 255, cv2.THRESH_BINARY)
cv2.imshow('image', image)
cv2.imshow('gray_image', gray_image)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)