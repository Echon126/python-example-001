import cv2
import item as item
import numpy as np
from PIL import Image, ImageEnhance
import os
import cv2

img = cv2.imread(r'C:\Users\ZKTT\Desktop\dt-Analysis\DDT_[00000000]_[20191221223211]_S00[01]\DDT4_1.jpg')
cv2.imshow('img', img)
rows, cols, channels = img.shape
dst = img.copy()

a = 1.2
b = 100
for i in range(rows):
    for j in range(cols):
        for c in range(3):
            color = img[i, j][c] * a + b
            if color > 255:
                dst[i, j][c] = 255
            elif color < 0:
                dst[i, j][c] = 0
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
