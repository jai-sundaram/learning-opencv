#blurring images can help with dealing with noise
#we know that anytime we are working with images or just data in general there will be a lot of noise
# There are four different functions for blurring
#blur(), GaussianBlur(), medianBlur(), bilateralFilter()

#everytime you are blurring an image think about averages
#when blurring, you are replacing each pixel with the average of all the pixels around it
#so again, replacing each pixel with the average of all the pixels in the neighborhood around it
#the way you find the average and what you define as the neighborhood around that given pixel will depend on that specific blurring

import os
import cv2

#read the photo
img = cv2.imread(os.path.join('.', 'data', 'stockphoto.jpg'))

#we can know define the size of the neighborhood
#now actually do the blurring
#first parameter is the image that we are blurring
#second parameter is the dimensions of the neighborhood that we are using to blur
#the higher these dimensions are, the stronger the blur
# we need to save this blurred image in a new variable
#note that this blurs the entire image
#Note that this is/ is called the classical blur
img_blur = cv2.blur(img, (30,30))
cv2.imshow('img_blur', img_blur)


#Gaussian Blur
#again the first field is the image, secon field is the neighborhood
#third field is the sigmaX, which I believe controls how much blurring is happening
img_gaus_blur = cv2.GaussianBlur(img, (7, 7), 3)
cv2.imshow('gaus_blur', img_gaus_blur)

#now we have Median Blurring
#for this we have to define a clear neighborhood size first
#k size must be an odd integer
k_size = 21
#now we can set up the blurring
median_blur = cv2.medianBlur(img, k_size)
cv2.imshow('median_blur', median_blur)

#denoising a noisy image
#we can use blurring to also denoisy images
img = cv2.imread(os.path.join('.', 'data', 'noisy.png'))
cv2.imshow('img', img)
denoised = cv2.medianBlur(img, 7)
cv2.imshow('denoised', denoised)
cv2.waitKey(0)
#we can see that blurring can somewhat help with denoising the image
#yes, its not completely perfect and the quality isnt great but atleast there's not that much noise now


