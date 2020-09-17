import cv2
import numpy as np

#Funcion convolucion
#Entrada: imagen
#Salida: muestra imagen con convolucion aplicando dos kernel: border y sharpen
def convolucion(image):
    kernel_border = np.array (([-1,-1,-1],[-1,8,-1],[-1,-1,-1]),np.float32) 
    kernel_sharpen = np.array (([0,-1,0],[-1,5,-1],[0,-1,0]),np.float32)

    output = cv2.filter2D (image,-1, kernel_border)
    output1 = cv2.filter2D (image,-1, kernel_sharpen)

    cv2.imshow("Imagen original", image) 
    cv2.imshow("Imagen con filtro: bordes", output)
    cv2.imshow("Imagen con filtro2: sharpen", output1)

def main():
    path = '/Users/lizbethmelendez/Downloads/OpenCVprueba/rueda.jpg'
    src = cv2.imread(path)
    image = cv2.cvtColor(src, cv2.COLOR_BGR2RGB) 
    convolucion(image)
