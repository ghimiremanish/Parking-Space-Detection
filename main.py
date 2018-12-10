#imports
import cv2
import numpy as np
import os
from polyPoints import polyPoints
from load_coordinate import load_coordinate
from crop_add_detect import crop_and_detect
import imutils

class main:
    def __init__(self):

        #load video
        self.cap = cv2.VideoCapture('dataset/1.mp4')

        #load cascade
        self.cascade_src = 'cars.xml'

        #load trained data
        self.car_cascade = cv2.CascadeClassifier(self.cascade_src)

    #load coordinate
    def load_coordinate(self):
        l = load_coordinate()
        return l.output()

    #croping image/frame
    def crop(self,frame,po):
        
        #croppppp
        # First find the minX minY maxX and maxY of the polygon
        m = po
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
        # finalImage = cropedImage[minY:maxY,minX:maxX]
        return cropedImage[minY:maxY,minX:maxX]


    def main(self):
        
        #saving points in roi
        roi = self.load_coordinate()

        #to count the total number of cars
        total_car_detected = 0

        while(True):
            
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            frame = imutils.resize(frame, width=450)
            # print roi
            if len(roi) == 0:
                print 'No Coordinates!!!'
                roi = self.load_coordinate()
            else:
                for m in roi:
                    vrx = np.array(m, np.int32)
                    vrx = vrx.reshape((-1,1,2))
                    frame = cv2.polylines(frame, [vrx], True, (0,255,255),3)
                    final = self.crop(frame,m)
                    
                    #check if car is found or not in final
                    cars = self.car_cascade.detectMultiScale(final, 1.1, 1)
                    if len(cars) != 0:
                        total_car_detected = total_car_detected + 1
                        print total_car_detected
                    
            # Display the resulting frame
            cv2.imshow('frame',frame)

            #exiting mechanism
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                print 'Quit'
                break
            elif key == ord('c'):
                print 'C is Pressed'

                #image is captured in realtime and saves in images/ folder
                cv2.imwrite('images/image.jpg',frame)

                #coordinate handler , calls and save coordinate data into coordinate.txt
                p = polyPoints()
                p.load()


m = main()
m.main()

# When everything done, release the capture
cv2.destroyAllWindows()