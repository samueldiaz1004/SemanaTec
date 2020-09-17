import numpy as np
import cv2

video = cv2.VideoCapture(0)

while True:
    ret,frame1 = video.read()
    frame = cv2.cvtColor(frame1,cv2.COLOR_RGB2BGR)
    frame_float = frame.astype(float)
    kernel1 = np.array([-0.5,0,0.5])
    kernel2 = np.array([[-0.5],[0],0.5])
    Hsx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    bordex = cv2.filter2D(frame_float)