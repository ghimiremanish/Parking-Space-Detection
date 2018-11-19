import numpy as np
import cv2

# mouse event handler
def mouse_drawing(event, x, y, flags, params):
     if event == cv2.EVENT_LBUTTONDOWN:
         print(x,y)

# Load an color image in grayscale
img = cv2.imread('test/test.jpg',1)

cv2.namedWindow("img")
cv2.setMouseCallback("img", mouse_drawing)



cv2.imshow('me',img)


k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('q'): # wait for 's' key to quit
    cv2.destroyAllWindows()
