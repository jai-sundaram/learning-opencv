import os
import cv2
#reading  image
img = cv2.imread(os.path.join('.', 'data', 'accord.jpg'))
#anytime you read an image in opencv using imread, it will be in the bgr  colorspace
#this means that every single pixel in this space is a combination of blue, red, and green

#however, we can convert an image to a differnet color space
#for example, we can convert it to rgb from bgr
#the difference betwen bgr and rgb is the order in which they are layed out btw

#here is how to convert the image
#using the cvtColor function
#first one is the image that we are converting, second field is from what to what
#make sure to save this under a new variable
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#you can think of colorspaces as different ways to represent an image
#or different ways to display the colors/information in an image
#by switching from BGR to RGB


#displaying the original image and the changed image
cv2.imshow('img', img)
cv2.imshow('img2', img_rgb)
cv2.waitKey(0)
#so now we are pretty miuch swapping the positions of red and blue when going from BGR to RGB
#everything that was red is now blue and everything that was blue is now red


#we could also convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#displayig the grayscale image
cv2.imshow('img_gray', img_gray)
cv2.waitKey(0)
#before the image had 3 channels, red,green,blue or blue/green/red
#now we are condensing all that into just one channel
#just gray

# we can now also do HSV which is another colorspace
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#now let us display the hsv image
cv2.imshow('img_hsv', img_hsv)
cv2.waitKey(0)

#different use cases for different colorspaces
