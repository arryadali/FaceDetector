import numpy as np
import cv2 as cv

path = r"C:\pemprog\python\ProjectFaceDetector\picture\myluv.jpg"

img = cv.imread(path, 1)
area_roi = img[1:200, 1:200]
cv.imshow("image roi", area_roi)
cv.waitKey(0)
cv.destroyAllWindows()