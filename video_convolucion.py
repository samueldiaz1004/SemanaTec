import cv2
import numpy as np

def camara():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    while (True):
        ret , frame = cap.read()
        image = cv2.cvtColor (frame, cv2.COLOR_BGR2RGB)
        image= convolucion (image)
        cv2.imshow ('frame',image)
        if cv2.waitKey (1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
        

def convolucion(image):
    kernel_border = np.array (([-1,-1,-1],[-1,8,-1],[-1,-1,-1]),np.float32) 
    kernel_sharpen = np.array (([0,-1,0],[-1,5,-1],[0,-1,0]),np.float32)

    output = cv2.filter2D (image,-1, kernel_border)
    output1 = cv2.filter2D (image,-1, kernel_sharpen)

    return output

def main():
    camara()

main()
    
