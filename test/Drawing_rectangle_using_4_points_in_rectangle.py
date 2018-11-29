import numpy as np
import cv2

point1 = ()
point2 = ()

#roi
roi = []

def on_mouse(event, x, y, flags, params):
	global point1,point2,roi
	if event == cv2.EVENT_LBUTTONDOWN:
		point1 = (x,y)
		print('point 1 :',point1)
	elif event == cv2.EVENT_BUTTONDOWN:
		point2 = (x,y)
		point1 = (x,y)
		print('point 2 :',point2)
		print('point 1: ', point1)
# load the image, clone it, and setup the mouse callback function
img = cv2.imread('test.jpg')
cv2.namedWindow("image")
cv2.setMouseCallback("image", on_mouse)

# keep looping until the 'q' key is pressed
while True:

	if len(point1) != 0 and len(point2) != 0:
		cv2.line(img,point1,point2,(255,0,0),5)
	
	# display the image and wait for a keypress
	cv2.imshow("image", img)
	
	
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		cv2.destroyAllWindows()
 
cv2.destroyAllWindows()