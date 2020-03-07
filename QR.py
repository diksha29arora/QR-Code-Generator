import numpy as np
import cv2 as cv

img = np.random.randint(0,2,(500,500))*255.

cv.imwrite("QR.png",img)