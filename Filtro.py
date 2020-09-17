import numpy as np
import cv2

video = cv2.VideoCapture(0)

while True:
    ret,frame1 = video.read()
    frame = cv2.cvtColor(frame1,cv2.COLOR_RGB2BGR)
    frame_float = frame.astype(float)
    kernel1 = np.array([-0.5,0,0.5])
    kernel2 = np.array([[-0.5],[0],[0.5]])
    Hsx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    Hsy = np.transpose(Hsx)
    bordex = cv2.filter2D(frame_float,-1,kernel1)
    bordey = cv2.filter2D(frame_float,-1,kernel2)
    Mxy = bordex**2+bordey**2
    Mxy = np.sqrt(Mxy)
    Mxy = Mxy/np.max(Mxy)
    mask = np.where(Mxy>0.1,255,0)
    mask2 = np.array(mask, dtype=np.uint8)
    cv2.imshow('Bordes',mask2)
    k = cv2.waitKey(1)&0xFF
    if (k == ord('p')):
        print('EL programa ha acabado')
        break
video.release()
cv2.destroyAllWindows()