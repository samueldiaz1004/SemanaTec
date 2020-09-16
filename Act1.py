import numpy as np
import cv2
import matplotlib.pyplot as plt

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

def sobel_x(pad): #Sobel en x
    sum = np.sum(pad[0]*[-1,0,1])
    sum += np.sum(pad[1]*[-2,0,2])
    sum += np.sum(pad[2]*[-1,0,1])
    return sum

def sobel_y(pad): #Sobel en y
    sum = np.sum(pad[0]*[1,2,1])
    sum += np.sum(pad[1]*0)
    sum += np.sum(pad[2]*[-1,-2,-1])
    return sum

######################################
### MAIN
######################################

###Guardar y leer la imagen como cv2
img = "/home/pedros/Documents/Jackie/yop.jpeg"
image = cv2.imread(img)

###Revisar que la imagen sea a blanco y negro
if len(image.shape) == 3: #si la imagen es de color (3 dimensiones)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #cambiar a blanco y negro (2 dimensiones)

img_row, img_col = image.shape
print(image)

convolution = np.zeros(image.shape) #numpy array con zeros del mismo tamano de la imagen para almacenar los resultados

###Modificar imagen con el kernel (Prewitt en y)
for i in range(img_row-3):
    for j in range(img_col-3):
        convolution[i][j] = prewitt_y(image[i:(i+3), j:(j+3)])
###Graficar y mostrar la imagen
plt.imshow(convolution, cmap='gray')
plt.title("Output Image using Prewitt in y")
plt.show()


###Modificar imagen con el kernel (Prewitt en x)
for i in range(img_row-3):
    for j in range(img_col-3):
        convolution[i][j] = prewitt_x(image[i:(i+3), j:(j+3)])
###Graficar y mostrar la imagen
plt.imshow(convolution, cmap='gray')
plt.title("Output Image using Prewitt in x")
plt.show()


###Modificar imagen con el kernel (Sobel en x)
for i in range(img_row-3):
    for j in range(img_col-3):
        convolution[i][j] = sobel_x(image[i:(i+3), j:(j+3)])
###Graficar y mostrar la imagen
plt.imshow(convolution, cmap='gray')
plt.title("Output Image using Sobel in x")
plt.show()


###Modificar imagen con el kernel (Sobel en y)
for i in range(img_row-3):
    for j in range(img_col-3):
        convolution[i][j] = sobel_y(image[i:(i+3), j:(j+3)])
###Graficar y mostrar la imagen
plt.imshow(convolution, cmap='gray')
plt.title("Output Image using Sobel in y")
plt.show()
