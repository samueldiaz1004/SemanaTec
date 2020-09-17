import cv2
import numpy as np

######################################
### FUNCIONES
######################################
def prewitt_y(pad): #Prewitt en y
    sum = np.sum(pad[0])
    sum += np.sum(pad[2]*-1)
    return sum

def prewitt_x(pad): #Prewitt en x
    sum = 0
    for i in range(3):
        sum += np.sum(pad[i]*[-1,0,1])
    return sum


######################################
### MAIN
######################################
video = "/home/jack/Videos/conejo.mp4"
video = cv2.VideoCapture(video)
count = 0

while video.isOpened() and count <= 40: #para que solo se procesen 40 imagenes del video y no este tan pesado
    count+=1
    ### Procesar el video
    (ret, frame) = video.read() #leer un frame del video
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #cambiar el frame a escala de grises

    ### Aplicar convolucion
    img_row, img_col = gray.shape
    image = np.zeros(gray.shape)
    image2 = np.zeros(gray.shape)
    ### Modificar imagen con el kernel (Prewitt en y)
    for i in range(img_row-3):
        for j in range(img_col-3):
            image[i][j] = prewitt_x(gray[i:(i+3), j:(j+3)])
            image2[i][j] = prewitt_y(gray[i:(i+3), j:(j+3)])

    ### Mostrar video
    cv2.imshow('Prewitt x', image)
    cv2.imshow('Prewitt y', image2)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()
