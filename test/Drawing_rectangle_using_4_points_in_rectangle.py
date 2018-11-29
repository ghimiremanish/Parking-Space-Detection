import numpy as np
import cv2

point = ()
point1 = ()
point2 = ()
point3 = ()
point4 = ()

click_count = 0
i = 1

def on_mouse(event, x, y, flags, params):
	global i,point1,point2,point3,point4,point
	if event == cv2.EVENT_LBUTTONDOWN:
		point = (x,y)
		if i is 1:
			point1 = (x,y)
		elif i is 2:
			point2 = (x,y)
		elif i is 3:
			point3 = (x,y)
		elif i is 4:
			point4 = (x,y)
			i = 0
		i = i + 1



# load the image, clone it, and setup the mouse callback function
img = cv2.imread('test.jpg')
cv2.namedWindow("image")
cv2.setMouseCallback("image", on_mouse)

# keep looping until the 'q' key is pressed
while True:

	#drwaing circle to show click feedback
	if len(point) != 0 :
		cv2.circle(img,point,5,(255,0,0),-1)
	
	# drawing rectangle
	# if len(point4) != 0:
	# 	cv2.rectangle(img, point1, point3, (0,255,0), 5)
	# 	point1 = ()
	# 	point2 = ()
	# 	point3 = ()
	# 	point4 = ()
	
	#drwing polygon
	if len(point4) != 0:
		vrx = np.array((point1,point2,point3,point4), np.int32)
		vrx = vrx.reshape((-1,1,2))
		img = cv2.polylines(img, [vrx], True, (0,255,255),3)
		point1 = ()
		point2 = ()
		point3 = ()
		point4 = ()

	# display the image and wait for a keypress
	cv2.imshow("image", img)
	
	
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		cv2.destroyAllWindows()
 
cv2.destroyAllWindows()