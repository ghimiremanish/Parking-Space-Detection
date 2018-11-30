import cv2
f = open('../coordinates.txt','r')

a = f.read()

# print(a)


img = cv2.imread('../images/image.jpg',1)

points = a
to = cv2.polylines(img, [points], True, (255,0,0), thickness=3)



cv2.imshow('image',to)
cv2.waitKey(0)
cv2.destroyAllWindows()