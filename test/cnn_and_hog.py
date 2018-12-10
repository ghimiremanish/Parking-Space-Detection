# import required packages
import cv2
import dlib
import time

# load input image
image = cv2.imread('images/image.jpg', 1)

if image is None:
    print("Could not read input image")
    exit()

cnn_car_detector = dlib.
