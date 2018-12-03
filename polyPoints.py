import numpy as np
import cv2

class polyPoints:

    #initializers
    def __init__(self):
        self.point = ()
        self.point1 = ()
        self.point2 = ()
        self.point3 = ()
        self.point4 = ()
        self.i = 1
        self.cord = []
    
    # mouse event handler
    def on_mouse(self,event, x, y, flags, params):
        global i,point1,point2,point3,point4,point
        if event == cv2.EVENT_LBUTTONDOWN:
            self.point = (x,y)
            # print self.point
            if self.i is 1:
                self.point1 = (x,y)
            elif self.i is 2:
                self.point2 = (x,y)
            elif self.i is 3:
                self.point3 = (x,y)
            elif self.i is 4:
                self.point4 = (x,y)
                self.i = 0
            self.i = self.i + 1

    # load the image, clone it, and setup the mouse callback function
    def load(self):
        img = cv2.imread('images/image.jpg')
        cv2.namedWindow("image")
        cv2.setMouseCallback("image",self.on_mouse)
        
        # keep looping until the 'q' key is pressed
        while True:
            #drwaing circle to show click feedback
            if len(self.point) != 0 :
                cv2.circle(img,self.point,5,(255,0,0),-1)

            #drwing polygon
            if len(self.point4) != 0:
                vrx = np.array((self.point1,self.point2,self.point3,self.point4), np.int32)

                #write in coordinates file
                #file open or append
                f = open('coordinates.txt', 'a')

                #file start wrinting
                f.write(str(vrx[0][0])+'\n')
                f.write(str(vrx[0][1])+'\n')
                f.write(str(vrx[1][0])+'\n')
                f.write(str(vrx[1][1])+'\n')
                f.write(str(vrx[2][0])+'\n')
                f.write(str(vrx[2][1])+'\n')
                f.write(str(vrx[3][0])+'\n')
                f.write(str(vrx[3][1])+'\n')
                f.close()

                vrx = vrx.reshape((-1,1,2))
                img = cv2.polylines(img, [vrx], True, (0,255,255),3)

                #reseting the value
                self.point1 = ()
                self.point2 = ()
                self.point3 = ()
                self.point4 = ()

            # display the image and wait for a keypress
            cv2.imshow("image", img)

            key = cv2.waitKey(1) & 0xFF
            # if the 's' key is pressed, save region and send back to video feed
            if key == ord("q"):
                f.close()
                cv2.destroyWindow('image')
                break