import numpy as np
import cv2

video = 'dataset/1.mp4'
prototxt = 'MobileNetSSD_deploy.prototxt.txt'
model = 'MobileNetSSD_deploy.caffemodel'

CLASSES = ["car"]

COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(prototxt, model)


cap = cv2.VideoCapture(video)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    (h, w) = frame.shape[:2]

    # blob = cv2.dnn.blobFromImage(cv2.resize(ima))
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843,
	(300, 300), 127.5)

    print("[INFO] computing object detections...")
    net.setInput(blob)
    detections = net.forward()

    # print detections
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.2:
            

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()