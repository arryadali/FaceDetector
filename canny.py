import numpy as np
import cv2 as cv

path = r"C:\pemprog\python\ProjectFaceDetector\picture\koin.jpg"

img = cv.imread(path, 0)
edges = cv.Canny(img, 10, 20)
cv.imshow("edges", edges)

cv.waitKey(0)
cv.destroyAllWindows()