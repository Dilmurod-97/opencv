import cv2
import numpy as np

img = cv2.imread('n1.jpg')

height, width = img.shape[:2]
new_width = 1000
new_height = int(new_width * height / width)
img = cv2.resize(img, (new_width, new_height))

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_img = cv2.medianBlur(gray_img, 5)
gray_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

edges = cv2.Canny(gray_img, 100, 200)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
