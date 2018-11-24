import cv2

cascade_src = 'cars.xml'
video_src = 'dataset/1.mp4'

#font
font = cv2.FONT_HERSHEY_SIMPLEX

#load video
cap = cv2.VideoCapture(video_src)

#load trained data
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    # converting to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # gussian blure to remove unnecessary noise
    # blur_gray = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=0)

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)


    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)

    # cv2.putText(img,"Number of faces detected: " + str(len(cars)),(500,40), font, 1,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(img,(str(len(cars))),(50,40), font, 1,(0,0,255),2,cv2.LINE_AA)

    cv2.imshow('video', img)

    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()