#imports
import cv2
import numpy as np
import os

#custom imports
from polyPoints import polyPoints
from loadCoordinates import loadCo

#initialize loadcoordinates
# def init():
#     c = loadCo()
#     data = c.output()
#     return data

#coordinates array
data = []

#data source
cascade_src = 'cars.xml'
video_src = 'dataset/1.mp4'

#font
font = cv2.FONT_HERSHEY_SIMPLEX

#load video
cap = cv2.VideoCapture(video_src)

#load trained data
car_cascade = cv2.CascadeClassifier(cascade_src)

#trigger init once
trigger = 0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    #if the file have some data draw rectangle
    if os.path.getsize('coordinates.txt') !=  0:

        #initializing data once 
        if len(data) is 0:
            c = loadCo()
            data = c.output()

        #printing each coordinates in video frame  with the help of numpy array
        for m in data:
            vrx = np.array(m, np.int32)
            vrx = vrx.reshape((-1,1,2))
            final= cv2.polylines(frame, [vrx], True, (0,255,255),3)

    #if the file has no data
    else:
        print 'No Coordinates'
        final = frame


    #print the image
    cv2.imshow('video feed', final)
    
    #if q is pressed then application is quited
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        # When everything done, release the capture
        print 'quit'
        cap.release()
        cv2.destroyAllWindows()
        break

    #if c is pressed then an image is capture on real time
    elif key == ord("c"):
        #image is captured and saves to db
        print 'c is pressed'
        p = polyPoints()
        p.load()
        trigger = 1