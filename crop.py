import numpy as np
import cv2

class crop:
    def main(self):
        #model
        prototxt = 'MobileNetSSD_deploy.prototxt.txt'
        model = 'MobileNetSSD_deploy.caffemodel'

        CLASSES = ["car"]

        # load our serialized model from disk
        print("[INFO] loading model...")
        net = cv2.dnn.readNetFromCaffe(prototxt, model)

        # m = coordinates
        m = ((48, 443), (196, 367), (446, 581), (243, 685))

        # Read a image
        I = cv2.imread('images/image.jpg')
        # I = frame

         # First find the minX minY maxX and maxY of the polygon
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
        finalImage = cropedImage[minY:maxY,minX:maxX]
        
        image = finalImage
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843,(300, 300), 127.5)
        
        # pass the blob through the network and obtain the detections and
        # predictions
        print("[INFO] computing object detections...")
        net.setInput(blob)
        detections = net.forward()

        # loop over the detections
        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0,0,i,2]
            # print type(confidence)
            if confidence >= 0.2:
                print 'confidence'
            else:
                print 'no detection'


        cv2.imshow('d',finalImage)

c = crop()
c.main()

cv2.waitKey(0)