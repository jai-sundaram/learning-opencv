#implementing edge detectors
#there are three algorithms to implement an edge detector in opencv
#one is the sobel operator, other one is the laplace edge detctor
#one is the canny edge detector
import os
import cv2
import numpy as np

img = cv2.imread(os.path.join('.', 'data', 'a90.jpeg'))
#first parameter is the iamge
#second parameter is the lower threshold - minimimum intensity gradient a pixel needs to have to be considered as part of the edge. any pixel with a value lower than this will be discarded
#third parameter is the upper threshold - max intensity gradient. any pixel above this will automatically be consdiered as part of the edge
img_edge =  cv2.Canny(img, 100, 200)

#there are two other functions that could be helpful as well

#this dilate functions will make the borders thhicker - it dilates the image
#first parameter is the image
#second parameter is the kernel that will pretty much be used for dilation
#the values in the array will control the actual thinkness, reducing it makes it less thick increasing it makes it more thick
#the dtypen controls what the data type, in this case it is int
img_edge_d = cv2.dilate(img_edge, np.ones((5,5),dtype=np.int8))

#cv2.erode
# as u can see the parameters are the same as it is for dilate
#this is the opposite of dilate, it makes the borders thinner than the original
# a larger kernel will lead to more erosion and a smaller kernel will lead to less erosion 
img_edge_c = cv2.erode(img_edge, np.ones((5,5), dtype= np.int8))






cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.waitKey(0)