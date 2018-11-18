import cv2
import numpy as np

point1 = ()
point2 = ()
point3 = ()
point4 = ()

# switch button
drawing = False

def mouse_drawing(event, x, y, flags, params):
        global point1,point2, drawing
        if event == cv2.EVENT_LBUTTONDOWN:
                if drawing is False:
                        drawing = True
                        point1 = (x, y)
                        print(point1,'point 1')
                else:
                        drawing = False
                
        elif event ==  cv2.EVENT_MOUSEMOVE:
                if drawing == True:
                        point2 = (x, y)
                        print(point2,'point 2')



cap = cv2.VideoCapture(0)

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse_drawing)


while True:
    _, frame = cap.read()

    #drawing rectangle
    if point1 and point2:
            cv2.line(frame, point1, point2, (0,255,0))
        #     cv2.rectangle(frame, point1, point2, (0,255,0))

    cv2.imshow("Frame", frame)



    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()