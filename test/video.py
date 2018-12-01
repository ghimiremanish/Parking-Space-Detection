import numpy as np
import cv2

cap = cv2.VideoCapture(0)
trigger = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if trigger == 1:
        print 'triggred'
        final = cv2.circle(frame, (100,100),50, (255,0,0))
    else:
        print 'not triggred'
        final = frame


    # Display the resulting frame
    cv2.imshow('frame',final)

    key = cv2.waitKey(1) & 0xFF
    if  key == ord('q'):
        break
    elif key == ord('g'):
        trigger = 1
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
