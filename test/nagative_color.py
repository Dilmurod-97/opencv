import cv2 as cv
import numpy as np

# Read the given image
img = cv.imread('img.jpg')

if img is not None:
    # Get its negative image
    img_nega = 255 - img
    
    # Get its vertically flipped image
    img_flip = img[::-1,:,:]
    
    # Show all images
merge = np.hstack((img, img_nega, img_flip))
cv.imshow('Image Editing: Original | Negative | Flip', merge)
cv.waitKey()
cv.destroyAllWindows()