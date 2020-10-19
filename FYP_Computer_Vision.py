# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:52:06 2020

@author: matt_
"""

import cv2
import numpy


cap = cv2.VideoCapture(0) #start the video capture
success, frame = cap.read()
cv2.namedWindow("MAIN")
iterations = 0
seconds = 60
fps = 27
while success:
    sucess, frame = cap.read() #reads the current frame
    if (iterations % (seconds*fps)) == 0:
        cv2.imwrite('capt2'+str(iterations/(seconds*fps))+'.jpg',frame)
    
    cv2.imshow('MAIN',frame) #display the main window
    if cv2.waitKey(1) & 0xFF == ord('q'): #end program with keypress of q
        break  
    iterations += 1
    print(iterations)
    
cap.release()
cv2.destroyAllWindows()
