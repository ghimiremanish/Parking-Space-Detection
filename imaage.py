import cv2
import numpy as np
from loadCoordinates import loadCo

c = loadCo()
data = c.output()

img = cv2.imread('images/image.jpg',1)

main = []
count = 0
for i in data:
    if count == 0:
        x1 = i
    elif count == 1:
        y1 = i
    elif count == 2:
        x2 = i
    elif count == 3:
        y2 = i
    elif count == 4:
        x3 = i
    elif count == 5:
        y3 = i
    elif count == 6:
        x4 = i
    elif count == 7:
        y4 = i
        main.append(((x1, y1), (x2, y2), (x3, y3), (x4, y4)))
        count = -1
    count = count + 1

for m in main:
    vrx = np.array(m, np.int32)
    vrx = vrx.reshape((-1,1,2))
    img = cv2.polylines(img, [vrx], True, (0,255,255),3)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()