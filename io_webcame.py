#working with webcams in this
import cv2

#we want to first to first like acess the webcam
#this 0 is the webcame we are acessing in the laptop
#if u only have one webcam (which i do) then it is is 0
webcam = cv2.VideoCapture(0)

#now to actually render the webcam
#this similair to working with a video
#while reading from a webcam, it is current so we never really reach the end we keeping having frames to read because again it is live
while True:
    #read from the webcam
    ret, frame = webcam.read()
    #ret should always be true

    #now let us actually show it
    cv2.imshow('frame', frame)

    #after capturing all the frames in this current iteration, wait 40 ms for a keypress of 'q'
    #if the key 'q' is pressed, then break out of the loop 
    if cv2.waitKey(40) & 0xFF == ord('q'):
        #this break statement makes out exist this loop
        break
#release the resources
webcam.release()
cv2.destroyAllWindows()
