import numpy as np
import cv2 as cv

path = r"C:\pemprog\python\ProjectFaceDetector\picture\koin.jpg"

img = cv.imread(path, 0)
blur = cv.GaussianBlur(img,(11,11),0)
edges = cv.Canny(blur, 10, 20)
dilated = cv.dilate(edges,(1,1), iterations=2)

(cnt, _) = cv.findContours(dilated.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print("jumlah koin {} dalam gambar".format(len(cnt)))

cv.imshow("coin", dilated)

cv.waitKey(0)
cv.destroyAllWindows()