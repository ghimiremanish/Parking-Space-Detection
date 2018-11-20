import numpy as np
import cv2

point = ()
def mouse_drawing(event, x, y, flags, params):
    global point

    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x, y)
        print(x,y)

# load the image, clone it, and setup the mouse callback function
img = cv2.imread('test.jpg')
cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_drawing)

# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
	cv2.imshow("image", img)
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		image = clone.copy()
 
	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		break


cv2.destroyAllWindows()