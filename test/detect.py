import cv2


img = cv2.imread('image1.jpg',1)

#load cascade
cascade_src = 'cars.xml'
#load trained data
car_cascade = cv2.CascadeClassifier(cascade_src)

# blur_gray = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=0)

cars = car_cascade.detectMultiScale(img, 1.1, 1)
            # print 'car detected'
for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)




cv2.imshow('man', img)
cv2.waitKey(0)