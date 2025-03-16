import os
import cv2

img = cv2.imread(os.path.join('.','su35.jpg'))
cropped_img = img[400:600, 400:800]

print(img.shape)
print(cropped_img.shape)

cv2.imshow('image',img)
cv2.imshow('cropped image', cropped_img)


cv2.waitKey(0)