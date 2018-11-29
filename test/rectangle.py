import numpy as np
import cv2

point1 = (384, 0)
point2 = (510, 128)

img = cv2.imread('test.jpg')

# cv2.rectangle(img, point1, point2, (80,18,236), 2)

cv2.line(img,(0,0),(511,511),(255,0,0),5)


cv2.imshow('rectangle on image', img) 


cv2.waitKey(0) 

cv2.destroyAllWindows()