import cv2
import os
import datetime

# init date
x = datetime.datetime.now()

img = cv2.imread('images/image.jpg',1)

n = 'image'+str(x.strftime('%M%S'))+'.jpg'
cv2.imwrite(n,img)

cv2.waitKey(0)