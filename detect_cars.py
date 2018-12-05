import cv2
import numpy as np
from loadCoordinates import loadCo

c = loadCo()
main = c.output()

# Read a image
I = cv2.imread('images/image.jpg')

count = 0
# Define the polygon coordinates to use or the crop
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
    print finalImage
    print 'finish'
    cascade_src = 'cars.xml'

    # #font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # #load trained data
    car_cascade = cv2.CascadeClassifier(cascade_src)


    gray = cv2.cvtColor(finalImage, cv2.COLOR_BGR2GRAY)

    # gussian blure to remove unnecessary noise
    blur_gray = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=0)

    cars = car_cascade.detectMultiScale(blur_gray, 1.1, 1)

    i = 0
    cars_det = []
    for (x,y,w,h) in cars:
        i = i+1
        cars_det.append((i))
        print i

    print cars_det
    cv2.imshow('video', blur_gray)
    n = 'manish'+str(count)+'.jpg'
    cv2.imwrite(n,blur_gray)
    count = count + 1
    
cv2.waitKey(0)
cv2.destroyAllWindows()