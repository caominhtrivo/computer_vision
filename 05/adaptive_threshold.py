import os
import cv2

image = cv2.imread(os.path.join('.','text.jpg'))
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
adpative_thresh = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 31)
ret, thresh = cv2.threshold(gray_image, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('image', image)
#cv2.imshow('gray_image', gray_image)
cv2.imshow('adpative_thresh', adpative_thresh)
cv2.imshow('thresh', thresh)

cv2.waitKey(0)