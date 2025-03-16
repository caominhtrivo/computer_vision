import os
import cv2

image = cv2.imread(os.path.join('.','noise_city.jpg'))
k_size = 9
blur_image = cv2.blur(image, (k_size, k_size))
gaussian_blue_image = cv2.GaussianBlur(image, (k_size, k_size), 5)
median_blue_image = cv2.medianBlur(image, k_size)
cv2.imshow('median_blue_image', median_blue_image)
cv2.imshow('gaussian_blue_image', gaussian_blue_image)
cv2.imshow('blur_image', blur_image)
cv2.imshow('image', image)
cv2.waitKey(0)