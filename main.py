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
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # drawing images
    if  os.path.getsize('coordinates.txt') != 0:
        print 'file have some data'
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
            final= cv2.polylines(frame, [vrx], True, (0,255,255),3)

        trigger = 1
    else:
        print 'no data in coordinates.txt'
        final = frame

    if trigger == 0:
        # cv2.destroyWindow('not triggred')
        # cv2.imshow('triggred',final)
        cv2.imshow('not triggred', final)
    else:
        # cv2.imshow('not triggred', final)
        cv2.imshow('triggred',final)



    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    #if c is pressed
    elif key == ord("c"):
        #image is captured and saves to db
        cv2.imwrite( "images/image.jpg", frame )
        p = polyPoints()
        p.load()
        

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
