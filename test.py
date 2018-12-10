#imports
import cv2
import numpy as np
import os

#custom imports
from polyPoints import polyPoints
from loadCoordinates import loadCo
from crop import crop
crp = crop()

data = []

#data source
video_src = 'dataset/1.mp4'
prototxt = 'MobileNetSSD_deploy.prototxt.txt'
model = 'MobileNetSSD_deploy.caffemodel'

CLASSES = ["car"]

print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(prototxt, model)

#load video
cap = cv2.VideoCapture(video_src)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    #if the file have some data draw rectangle
    if os.path.getsize('coordinates.txt') !=  0:
        #initializing data once 
        if len(data) is 0:
            c = loadCo()
            data = c.output()
        count = 0
        #printing each coordinates in video frame  with the help of numpy array
        for m in data:
            vrx = np.array(m, np.int32)
            vrx = vrx.reshape((-1,1,2))
            final= cv2.polylines(frame, [vrx], True, (0,255,255),3)
            # crp.main(frame,m)
            #croppppp
            # First find the minX minY maxX and maxY of the polygon
            I = frame
            minX = I.shape[1]
            maxX = -1
            minY = I.shape[0]
            maxY = -1
            for point in m:
                x = point[0]
                y = point[1]

                if x < minX:
                    minX = x
                if x > maxX:
                    maxX = x
                if y < minY:
                    minY = y
                if y > maxY:
                    maxY = y
            
            # Go over the points in the image if thay are out side of the emclosing rectangle put zero
            # if not check if thay are inside the polygon or not
            cropedImage = np.zeros_like(I)
            for y in range(0,I.shape[0]):
                for x in range(0, I.shape[1]):

                    if x < minX or x > maxX or y < minY or y > maxY:
                        continue

                    if cv2.pointPolygonTest(np.asarray(m),(x,y),False) >= 0:
                        cropedImage[y, x, 0] = I[y, x, 0]
                        cropedImage[y, x, 1] = I[y, x, 1]
                        cropedImage[y, x, 2] = I[y, x, 2]

            # Now we can crop again just the envloping rectangle
            finalImage = cropedImage[minY:maxY,minX:maxX]
            n = 'man'+str(count)
            count = count + 1
            cv2.imshow(n,finalImage)
            image = finalImage
            (h, w) = image.shape[:2]
            blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843,(300, 300), 127.5)
            print("[INFO] computing object detections...")
            net.setInput(blob)
            detections = net.forward()
            confidence = detections[0,0,0,2]
            if confidence > 0.4:
                # print 'detected'
                print confidence
            elif confidence < 0.4:
                print 'not detected'

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