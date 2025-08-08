import cv2
import os

#first let us pretty much define the image path
#this will help us actually get that iamge
img_path = os.path.join('.', 'data', 'scatpack.jpg')
#now let us read the image
#use the imread function to actually read the image
img = cv2.imread(img_path)
#now just for testing, we will be saving the same age agin in the same place pretty much
#use the imwrite function to write/save an image
#first parameter is where we are saving it, second parameter is the image we are saving
cv2.imwrite(os.path.join('.', 'data', 'scatpack_new.jpg'), img)
#now we can actually render the image here
#first parameter is the name of the window in which we are going to visualize the image
#by the way we are setting the name, this isnt something that already exists
#2nd parameter is the actual image
cv2.imshow('image', img)
#now this following statement is actually very important for it to actually show, otherwise it will just immediately show and then close the winopw
#with this number as 0, it just means that opencv is going to wait indefinitely with the window open
cv2.waitKey(0)