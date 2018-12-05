import cv2
import numpy as np
import datetime
import os
from loadCoordinates import loadCo

class crop:
    
    def __init__(self):
        # init date
        self.x = datetime.datetime.now()

        # Read a image
        self.I = cv2.imread('images/image.jpg')

    def load_coordinates(self):
        c = loadCo()
        data = c.output()
        return data



    def main(self):
        # # First find the minX minY maxX and maxY of the polygon
        minX = self.I.shape[1]
        maxX = -1
        minY = self.I.shape[0]
        maxY = -1

        polygon = self.load_coordinates()
        for point in polygon:
            x = point[0][0]
            y = point[0][1]
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
            cropedImage = np.zeros_like(self.I)
            for y in range(0,self.I.shape[0]):
                for x in range(0, self.I.shape[1]):

                    if x < minX or x > maxX or y < minY or y > maxY:
                        continue
                    print np.asarray(point[0])
                    if cv2.pointPolygonTest(np.asarray(point[0]),(x,y),False) >= 0:
                    #     cropedImage[y, x, 0] = self.I[y, x, 0]
                    #     cropedImage[y, x, 1] = self.I[y, x, 1]
                    #     cropedImage[y, x, 2] = self.I[y, x, 2]

            # Now we can crop again just the envloping rectangle
            # finalImage = cropedImage[minY:maxY,minX:maxX]
            # print finalImage
            
            #writing image to images/cropped folder according to minute and second
            # n =  'image'+self.x.strftime('%M%S')+'.jpg'
            # cv2.imwrite(os.path.join('images/cropped/',n),finalImage)


c = crop()
c.main()