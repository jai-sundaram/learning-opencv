#now we are going to focus on working with videos
import os
import cv2

#first let us get the video path
video_path = os.path.join('.', 'data', 'vette.mp4')

#now let us read the video
video = cv2.VideoCapture(video_path)

#now let us try to render the video

#we are going to pretty much be reading the video frame by frame
ret = True
#the ret variable is a boolean variable that says if the frame is sucessfully read or not
while ret == True:
    #frame is the actual frame
    ret, frame = video.read()
    #first all we want to execute this only if the frame is actually sucessfully read
    #let us show the frame
    cv2.imshow('frame', frame)
    #we want to wait to wait the amount of time of like how often one frame happens
    #now in this case we know that this video is 24fps (can see in file explorer)
    #So, 1/24 = 0.041 = 41 millseconds
    #so wait for 41 milliseconds
    #this makes it so that the video actually plays at the correct playback speed - 24fps
    #so basically one frame takes 41 ms, so wait 41 ms between each frame
    cv2.waitKey(41)
#these lines actually makes sure that like we actually end and exit out of the video
#frees up the resources that were used for the video
video.release()
#destroy the window that was created by opencv
cv2.destroyAllWindows()
