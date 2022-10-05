import cv2 as cv
import numpy as np

# reading image
img = cv.imread('1.png')

# edges
gray = cv.cvtColor(img, cv.COLOR_BAYER_BG2GRAY)
gray = cv.medianBlur(gray, 5)
edges = cv.adaptiveThreshold(gray, 255,
        cv.ADAPTIVE_THRESH_MEAN_C,
        cv.THRESH_BINARY, 9, 9)

#cartoonization
color = cv.bilateralFilter(img, 9, 250, 250)
cartoon = cv.bitwise_and(color, color, mask=edges)

cv.imshow('Image', img)
cv.imshow('edges', edges)
cv.imshow('Cartoon', cartoon)

cv.waitKey(0)
cv.destroyAllWindows()