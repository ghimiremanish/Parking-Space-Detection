#imports
import cv2
import numpy as np
import os

#custom imports
from polyPoints import polyPoints
from loadCoordinates import loadCo

#initialize loadcoordinates
c = loadCo()
data = c.output()

#data source
cascade_src = 'cars.xml'
video_src = 'dataset/1.mp4'

#font
font = cv2.FONT_HERSHEY_SIMPLEX

#load video
cap = cv2.VideoCapture(video_src)

#load trained data
car_cascade = cv2.CascadeClassifier(cascade_src)

#triggring mechanism
trigger = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    cv2.imshow('triggred',frame)







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
        