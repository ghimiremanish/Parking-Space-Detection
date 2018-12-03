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


        return arr