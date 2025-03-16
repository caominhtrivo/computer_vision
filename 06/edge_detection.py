import os
import cv2
import numpy as np

image = cv2.imread(os.path.join('.','t14.jpg'))
edge_image = cv2.Canny(image, 180, 200)
edge_dilate_image = cv2.dilate(edge_image, np.ones((3,3), dtype = np.int8))
edge_erode_image = cv2.erode(edge_dilate_image, np.ones((3,3), dtype = np.int8))

cv2.imshow('image', image)
cv2.imshow('edge_image', edge_image)
cv2.imshow('edge_dilate_image', edge_dilate_image)
cv2.imshow('edge_erode_image', edge_erode_image)


cv2.waitKey(0)