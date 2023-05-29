import cv2 as cv
import numpy as np

path = r"C:\pemprog\python\ProjectFaceDetector\picture\monkey.jpg"
img = cv.imread(path, 0)
cv.imshow('kong', img)
cv.waitKey(0)
cv.imwrite('gambar2.jpg', img)
cv.destroyAllWindows()