import cv2
import imutils
import numpy as np

def process_picture(img):
    img = imutils.resize(img, height=500)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    edged_img = cv2.Canny(blurred_img, 100, 200)
    return edged_img

zero = cv2.imread('0.png')
zero = process_picture(zero)
cv2.imshow('Zero', zero)
zero = imutils.resize(zero, height=500)
grayZero = cv2.cvtColor(zero, cv2.COLOR_BGR2GRAY)
blurredZero = cv2.GaussianBlur(grayZero, (5, 5), 0)
edgedZero = cv2.Canny(blurredZero, 100, 200)
cv2.imshow('Edged', edgedZero)
cv2.imwrite('EdgedZero.png', edgedZero)

one = cv2.imread('1.png')
cv2.imshow('One', one)
one = imutils.resize(one, height=500)
grayOne = cv2.cvtColor(one, cv2.COLOR_BGR2GRAY)
blurredOne = cv2.GaussianBlur(grayOne, (5, 5), 0)
edgedOne = cv2.Canny(blurredOne, 100, 200)
cv2.imshow('Edged', edgedOne)
#cv2.imwrite('EdgedOne.png', edgedOne)

cv2.waitKey(0)