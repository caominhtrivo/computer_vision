import os
import cv2

image = cv2.imread(os.path.join('.','board.jpg'))
print(image.shape)
image = cv2.resize(image, (1200, 800))

#line
cv2.line(image, (0,0), (200, 200), (255,0,0), 2)

#redtangle
cv2.rectangle(image, (200,300), (500, 700), (50,100,200), -1)

#circle
cv2.circle(image, (600, 400), 200 ,(255,0,255), 10)

#text
cv2.putText(image, 'Vietnam No.1', (500,500), cv2.FONT_HERSHEY_COMPLEX, 3, (0,0,255), 10)

cv2.imshow('image', image)
cv2.waitKey(0)