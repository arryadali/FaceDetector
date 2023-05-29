import cv2 as cv

cap = cv.VideoCapture(0)
face = cv.CascadeClassifier("ProjectFaceDetector\haarcascade_frontalface_default.xml")
eye = cv.CascadeClassifier("ProjectFaceDetector\haarcascade_eye.xml")

while True:
    ret, frame = cap.read()

    frame = cv.cvtColor(frame, 0)

    detections = face.detectMultiScale(frame)

    if(len(detections) > 1):
        (x,y,w,h) = detections[0]
        frame = cv.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)

    cv.imshow("frame", frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.realease()
cv.waitKey(0)
cv.destroyAllWindows()