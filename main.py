#imports
import cv2
import numpy as np

#data source
cascade_src = 'cars.xml'
video_src = 'dataset/1.mp4'

#font
font = cv2.FONT_HERSHEY_SIMPLEX

#load video
cap = cv2.VideoCapture(video_src)

#load trained data
car_cascade = cv2.CascadeClassifier(cascade_src)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('me',frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    #if c is pressed
    elif key == ord("c"):
        #image is captured
        img = cv2.imshow('Capture', frame)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
