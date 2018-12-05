import cv2
import numpy as np
class loadCo:
    f = open('coordinates.txt','r')

    def output(self):

        points = self.f.read()
        
        s = points.split()
        arr = []
        for a in s:
            arr.append(int(a))

        main = []
        count = 0
        for i in arr:
            if count == 0:
                x1 = i
            elif count == 1:
                y1 = i
            elif count == 2:
                x2 = i
            elif count == 3:
                y2 = i
            elif count == 4:
                x3 = i
            elif count == 5:
                y3 = i
            elif count == 6:
                x4 = i
            elif count == 7:
                y4 = i
                main.append(((x1, y1), (x2, y2), (x3, y3), (x4, y4)))
                count = -1
            count = count + 1

        return main




# c = loadCo()
# data = c.output()

# frame = cv2.imread('images/image.jpg',1)

# for m in data:
#     vrx = np.array(m, np.int32)
#     vrx = vrx.reshape((-1,1,2))
#     frame= cv2.polylines(frame, [vrx], True, (0,255,255),3)

# cv2.imshow('final',frame)
# cv2.waitKey(0)
