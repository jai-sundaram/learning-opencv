import cv2
import os

#first we are going to be using a whiteboard image  so that we have something to actually draw on
whiteboard = cv2.imread(os.path.join('.', 'data', 'whiteboard.jpg'))
print(whiteboard.shape)

#drawing a line
#to draw a line simply use the line function
#the first parameter is the image we are drawing on
#second paraemter is the (x,y) coordinate where the line should start
#the third parameter is the (x,y) coordinate where the line should end
#the the fourth parameter specifies the color of the line in BGR format - in this case it is green
#fifth parameter is the thickness of the line
cv2.line(whiteboard, (100, 150), (200, 250), (0,250, 0), 3)


#now drawing a rectangle
#use the rectangle function
#first parameter is the image
#second parameter is the starting coordinate (the top left point of the rectangle)
#third parameter is the ending coordinate (the bottom right point of the rectangle)
#the fourth parameter is the color in BGR format - in this case it is blue
#the sixth  parameter is the thickness of the rectangle
#by the way if we passed in the thickness of the rectangle was -1
cv2.rectangle(whiteboard, (200, 200), (300, 300), (250, 0, 0), -1)


#now drawing a circle
#the second parameter is the coordinates for the center of the circle
#the third parameteter is the radius of the circle
#the fourth parameter is the color of the circle again in BGR format
#the fifth parameter is the thickness of the circle
cv2.circle(whiteboard, (400,200), 10, (0,0,255), 3)

#now we can also add text to an image
#use the putText function
#the first parameter is the image where we are putting this on
#the second parameter is the message
#the third parameter is the position of the text
#the fourth parameter is the type of font for the message
#the fifth parameter is the size of the text
#the sixth parameter is the color of the font
#the seventh parameter is the texture of the font
cv2.putText(whiteboard, 'Hello',(360, 130), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 0), 10)




cv2.imshow('whiteboard', whiteboard)
cv2.waitKey(0)