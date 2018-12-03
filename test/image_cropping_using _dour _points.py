# import cv2

# cascade_src = 'cars.xml'
# image_src = 'images/image.jpg'

# #load image
# img = cv2.imread(image_src,0)

# # #font
# font = cv2.FONT_HERSHEY_SIMPLEX

# #load cascade
# car_cascade = cv2.CascadeClassifier(cascade_src)


# cars = car_cascade.detectMultiScale(img, 1.1, 1)


# for (x,y,w,h) in cars:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
#     # cv2.putText(img,"Number of faces detected: " + str(len(cars)),(500,40), font, 1,(0,0,255),2,cv2.LINE_AA)
#     cv2.putText(img,(str(len(cars))),(50,40), font, 1,(0,0,255),2,cv2.LINE_AA)
#     cv2.imshow('video', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

# Read a image
I = cv2.imread('images/image.jpg')

# Define the polygon coordinates to use or the crop
polygon = [[[20,110],[450,108],[340,420],[125,420]]]

# First find the minX minY maxX and maxY of the polygon
minX = I.shape[1]
maxX = -1
minY = I.shape[0]
maxY = -1
for point in polygon[0]:

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

# cv2.imwrite('finalImage.png',finalImage)
cv2.imshow('f',finalImage)