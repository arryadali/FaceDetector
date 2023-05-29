import numpy as np
import cv2 as cv

path = r"C:\pemprog\python\ProjectFaceDetector\picture\myluv.jpg"

img = cv.imread(path, 1)

ukuranx, ukurany = img.shape[1]/2, img.shape[0]/2
img_baru = cv.resize(img, (ukuranx, ukurany))

cv.imshow("image sebelum di rize", img)
cv.imshow("image setelah di risize", img_baru)

cv.waitKey(0)
cv.destroyAllWindows()