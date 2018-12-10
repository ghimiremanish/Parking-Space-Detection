import cv2
import numpy as np
import os
from loadCoordinates import loadCo

class crop:

    def main(self,img):
        
        # #load cascade
        # cascade_src = 'cars.xml'

        # #load trained data
        # car_cascade = cv2.CascadeClassifier(cascade_src)

        # Read a image
        I = cv2.imread('images/image.jpg')

        #load coordinates
        d = loadCo()
        main = d.output()

        #count the number of cars
        co = 0

        #to get multiple crops
        for m in main:
            polygon = m
            
            # First find the minX minY maxX and maxY of the polygon
            minX = I.shape[1]
            maxX = -1
            minY = I.shape[0]
            maxY = -1
            for point in polygon:
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

                    if cv2.pointPolygonTest(np.asarray(polygon),(x,y),False) >= 0:
                        cropedImage[y, x, 0] = I[y, x, 0]
                        cropedImage[y, x, 1] = I[y, x, 1]
                        cropedImage[y, x, 2] = I[y, x, 2]

            # Now we can crop again just the envloping rectangle
            finalImage = cropedImage[minY:maxY,minX:maxX]

            # cv2.imwrite('image'+str(co)+'.jpg',finalImage)
            co = co + 1
        #     gray = cv2.cvtColor(finalImage, cv2.COLOR_BGR2GRAY)

        #     # gussian blure to remove unnecessary noise
        #     blur_gray = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=0)

        #     cars = car_cascade.detectMultiScale(blur_gray, 1.1, 1)
        #     # print 'car detected'

        #     if len(cars) != 0:
        #         co = co + 1
            
        # # return co
        # print co



c = crop()
c.main()