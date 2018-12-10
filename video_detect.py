#imports
import cv2
import numpy as np
import os

from loadCoordinates import loadCo
c = loadCo()
data = c.output()

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
        for m in data:
            

    else:
        print '[INFO] No Coordinates'

cv2.waitKey(0)
cv2.destroyAllWindows()