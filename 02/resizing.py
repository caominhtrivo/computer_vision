import cv2
import os

img = cv2.imread(os.path.join('.','su35.jpg'))
resized_img = cv2.resize(img, (600, 400)) #height then width

print(img.shape)
print(resized_img.shape)

cv2.imshow('image',img)
cv2.imshow('resized image',resized_img)
cv2.waitKey(0)