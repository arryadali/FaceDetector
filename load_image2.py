import cv2 as cv
import numpy as np

path = r"C:\pemprog\python\ProjectFaceDetector\picture\arrya.png"

#read the image
img = cv.imread(path, cv.IMREAD_COLOR)
#change the size
cv.namedWindow("Ini adalah cewe aku pas kecil", cv.WINDOW_NORMAL)
#displaying the image
cv.imshow("Ini adalah cewe aku pas kecil", img)
#
cv.waitKey(0)
#displaying to window
cv.destroyAllWindows()