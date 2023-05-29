import numpy as np
import cv2 as cv

path1 = r"C:\pemprog\python\ProjectFaceDetector\picture\monkey.jpg"
img1 = cv.imread(path1, 1)

path2 = r"C:\pemprog\python\FD\myluv.jpg"
img2 = cv.imread(path2, 1)

path3 = r"C:\pemprog\python\FD\aing.png"
img3 = cv.imread(path3, 1)

cv.imshow("image 1", img1)
cv.imshow("image 2", img2)
cv.imshow("image 3", img3)

cv.waitKey(0)
cv.destroyAllWindows()