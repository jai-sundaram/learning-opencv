import os
import cv2

#getting the path again
img_path = os.path.join('.', 'data', 'raptor.jpg')
#getting the image itself
img = cv2.imread(img_path)

#showing the image
cv2.imshow('image', img)
cv2.waitKey(0)

#printing current image size
print(img.shape)

#cropping the image
#to basically crop the image, we are pretty much specifying which portions of the original photo must be included
#so for example, for the height, if we are to say 300:900 nothing under the 300 mark will be included and nothing after the 900 mark will be included
#Similairly, for the width, if we were to say 300:1200 then nothing left of 300 will be included and nothing right of 1200 will be included
cropped_img = img[600:900, 300:1200]
cv2.imshow('cropped', cropped_img)
cv2.waitKey(0)
