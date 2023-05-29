import numpy as np
import cv2 as cv

wajahPath = r"C:\pemprog\python\ProjectFaceDetector\haarcascade_frontalface_default.xml"
wajah = cv.CascadeClassifier(wajahPath)
mataPath = r"C:\pemprog\python\ProjectFaceDetector\haarcascade_eye.xml"
mata = cv.CascadeClassifier(mataPath)

path = r"C:\pemprog\python\ProjectFaceDetector\picture\percobaan1wajah.jpg"

img = cv.imread(path)
img_gray = cv.cvtColor(img, cv.IMREAD_COLOR)

deteksi_wajah = wajah.detectMultiScale(img_gray, 1.3, 5)

for(x,y,w,h) in deteksi_wajah:
    cv.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
    roi_gray = img_gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    deteksi_mata = mata.detectMultiScale(roi_gray)

    for(ex, ey, ew, eh) in deteksi_mata:
        cv.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),2)

cv.namedWindow("path", cv.WINDOW_NORMAL)
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()