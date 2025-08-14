import os
import cv2

#first let us read the image
img = cv2.imread(os.path.join('.', 'data', 'birds.jpg'))
#first we are going to convert this to a grayscale image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#first we are going to apply a threshold
#in this case we are going to have a black background like white stuff on top of that
#so we do thresh_binary_inv where we take everything less than 127 to 255 and everything more than that to 255
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

# and this being white on top of black will help us actually work with contours
#countours are pretty much curves that join all the points along a boundary and they tend to have the same intensity or color
#they are pretty much like the outliers of an object
#in this particular use case we are pretty much detecting all the birds in an image
#that is why we invert the thresholding so the background is black and the objects are white
#this makes them easier to detect

#now we are going to be extracting the countours in this image
#again in this case the countours are pretty much the white regions and they are the birds so
#again the countour is self explanatory
#the hierarchy is pretty much a numpy array that describes the parent child relationship between the countors
#each countour has a Next, Previous, First_Child, Parent attribute
#cv2.RETR_TREE will decide how the contours are organized
#cv2.CHAIN_APPROX_SIMPLE will decide how many points are stored in the countours

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#when getting the contours we also get a lot of noise as well
#however, to distinguish the noise from the actual data, we will look at the size of the countours
#if the area of the countour is quite big, lets say  bigger than like 200,  then it is most likely real data/contours
#otherwise, if it is very smaller like smaller than 200 for instance it is most likely just noise

#to see if it, we will be drawing the valid contours on top of the original image
for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        #first parameter is the image we are drawing on top of
        # #second parameter is just -1 , remember that
        # #third parameter is the color '
        #fourth parameter is the thickness
        # cv2.drawContours(img, cnt, -1, (0, 255, 0), 1)

        #now we are going to do like a object detector/bounding box for the contours
        #first get the (x1,y1) and the width and height  for the contours
        #we will be using this to draw the bounding box/rectangle for the contours
        x1, y1, w, h = cv2.boundingRect(cnt)
        # we only get w and h
        #to get x2 from x1 and w simply do x2 = x1 + w
        #to get y2 from x2 and h simply do y2 = y1 + h

        cv2.rectangle(img,(x1,y1), (x1 + w, y1 + h), (0, 255, 0), 2)

    #as u can see u can use contours to do object detection 


cv2.imshow('thresh', thresh)
cv2.imshow('img', img)
cv2.waitKey(0)