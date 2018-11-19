import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    #text inserting
    font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(frame,'Press C toCapture Image',(5,50), font, 1,(0,0,255),2,cv2.LINE_AA)
    
    # Display the resulting frame
    cv2.imshow('me',frame)
    
    
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    elif key == ord("c"):
        img = cv2.imshow('Capture', frame)
        

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()