import os
import cv2

image = cv2.imread(os.path.join('.','test.jpg'))
image = cv2.resize(image, (1200, 800))
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        cv2.drawContours(image, cnt, -1, (0, 255, 0), 1)
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,0), 4)

cv2.imshow('image', image)
#cv2.imshow('gray_image', gray_image)
#cv2.imshow('thresh', thresh)

cv2.waitKey(0)