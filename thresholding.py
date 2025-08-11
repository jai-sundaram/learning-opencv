#thresholding can be used to convert a regular image to a binary image

import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'escalade.jpg'))
cv2.imshow('img', img)


#converting this to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#now we will be setting the threshold
#in this, the first parameter in the function is the actual image
#the second value is the threshold, meaning that any pixels with a value less than this value will be set to 0
#the third value is the basically the value that a pixel should be set to if it is greater than the threshold value
#the fourth parameter pretty much speciifes that in this case the thresholding is for a binary image
#this will return two different values, ret and thresh
#btw this is a global threshold and pretty straightforward, all pixels above the threshold are white and all pixels before the threshold are black
#it will be constant
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
cv2.imshow('img_gray', img_gray)
cv2.imshow('thresh', thresh)

#thresholding can be used to segment your image


#after thresholding, we can blur the image to reduce noise
thresh = cv2.blur(thresh, (5, 5))
cv2.imshow('thresh_blur', thresh)

#when it is harder to set a basic thresshold globally, where it is hard to decipher what the threshold should be, we use adaptive thresholds
handwriting_img = cv2.imread(os.path.join('.', 'data', 'handwriting.jpg'))

#first convert it to grayscale
handwriting_gray = cv2.cvtColor(handwriting_img, cv2.COLOR_BGR2GRAY)
#with adaptive thresholds opencv will figure out the threshold by itself
#this can be helpful again in tricky scennarios where it can be hard to figure out the exact thresholds
#there are only a few  things we will be passing in
#first one is the image that we are applying this threshold to
#the second one is the value we should take pixels to if the pixel is currently higher than the threshold opencv computes
#the third one is the type of adaptive threshold, one is gaussian and one is mean
#the fourth one is the thresholding type - thresh_binary
#fifth parameter is the size of the neighborhood that must be used to calculate the threshold for a pixel - has to be odd
#the sixth parameter is the constant that is subtracted from the mean of the neighborhood pixels - has to be even
#increasing the sixth parameter will make the result darker, decreasing it will make it lighter
thresh = cv2.adaptiveThreshold(handwriting_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)



cv2.imshow('thresh', thresh)
cv2.waitKey(0)

