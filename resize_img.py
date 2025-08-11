#resizing an image
import cv2
import os

img_path = os.path.join(".", "data", "raptor.jpg")
img = cv2.imread(img_path)

#getting the image shape
print(img.shape)

#rendering the image
# cv2.imshow('img', img)
# cv2.waitKey(0)

# now let us try to resize this image
#first parameter is the image
#second parameter is the size that the new image should be
#for resizing:            height, width
resize_img = cv2.resize(img, (60, 50))
#for getting the actual shape: width, height, number of channels
print(resize_img.shape)
cv2.imshow('resize_img', img)
cv2.waitKey(0)
