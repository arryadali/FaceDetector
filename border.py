import cv2 as cv
import numpy as np

path = r"C:\pemprog\python\ProjectFaceDetector\picture\arrya.png"

img = cv.imread(path, cv.IMREAD_COLOR)
cv.copyMakeBorder(img, 100, 100, 100, 100, cv.BORDER_REFLECT)
cv.imshow("Ini adalah cewe aku pas kecil", img)
cv.waitKey(0)
cv.destroyAllWindows()