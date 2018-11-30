import cv2
import numpy as np
class loadCo:
    f = open('coordinates.txt','r')

    def output(self):
        # return (self.f.read())
        
        # c = loadCo()

        points = self.f.read()

        # data manupulating to array
        b = ''

        #for storing stings
        val = []
        # final array list of polygon 
        arr = []

        #count
        c = 0

        for p in points:
            #rrmoving impurities from text to get numbers
            if p != '[' and p != '(' and p != ',' and p != ')' and p != ' ' and p != ']':
                val.append(p)

        for i in val:
            b = b + i
            c = c + 1
            if c == 3:
                arr.append(int(b))
                b = ''
                c = 0
        
        return arr


c = loadCo()
print(c.output())

img = cv2.imread('images/image.jpg',1)

points = 
to = cv2.polylines(img, [points], True, (255,0,0), thickness=3)



cv2.imshow('image',to)
cv2.waitKey(0)
cv2.destroyAllWindows()