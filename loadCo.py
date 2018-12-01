import cv2
import numpy as np
class loadCo:
    f = open('coordinates.txt','r')

    def output(self):

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
            #removing impurities from text to get numbers
            if p != '[' and p != '(' and p != ',' and p != ')' and p != ' ' and p != ']':
                val.append(p)

        
        # for i in val:
        #     b = b + i
        #     c = c + 1
        #     if c == 3:
        #         arr.append(int(b))
        #         b = ''
        #         c = 0
        
        # return arr


c = loadCo()
print(c.output())
