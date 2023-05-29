import numpy as np
import cv2 as cv

path = r"C:\pemprog\python\ProjectFaceDetector\picture\monkey.jpg"

img = cv.imread(path, 1)
lebar, tinggi = img.shape[0], img.shape[1]
putar = cv.getRotationMatrix2D((lebar/2, tinggi/2),180,1)
img_putar = cv.warpAffine(img, putar,(lebar, tinggi))
cv.imshow("foto yang diputar", img_putar)

cv.waitKey(0)
cv.destroyAllWindows()