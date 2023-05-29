import numpy as np
import cv2 as cv

path = r"C:\pemprog\python\ProjectFaceDetector\picture\myluv.jpg"

img = cv.imread(path, cv.IMREAD_COLOR)
print("Lebar foto : ", img.shape[1])
print("Tinggi foto : ", img.shape[0])