# import cv2

# cascade_src = 'cars.xml'
# video_src = 'dataset/1.mp4'

# #font
# font = cv2.FONT_HERSHEY_SIMPLEX

# #load video
# cap = cv2.VideoCapture(video_src)

# #load trained data
# car_cascade = cv2.CascadeClassifier(cascade_src)

# while True:
#     ret, img = cap.read()
#     if (type(img) == type(None)):
#         break
#     # converting to gray
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # gussian blure to remove unnecessary noise
#     # blur_gray = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=0)

#     cars = car_cascade.detectMultiScale(blur_gray, 1.1, 1)


#     for (x,y,w,h) in cars:
#         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)

#     # cv2.putText(img,"Number of faces detected: " + str(len(cars)),(500,40), font, 1,(0,0,255),2,cv2.LINE_AA)
#     cv2.putText(img,(str(len(cars))),(50,40), font, 1,(0,0,255),2,cv2.LINE_AA)

#     cv2.imshow('video', img)

#     if cv2.waitKey(33) == 27:
#         break

# cv2.destroyAllWindows()

import cv2
import numpy as np

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)





img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()