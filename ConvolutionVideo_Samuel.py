import cv2
import numpy as np

# Asignar la camara por default en computadora
cap = cv2.VideoCapture(0)
# Codec; parametro necesario para output de video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# Output de video (Nombre de archivo, codec, fps, tamaño de ventana)
# Por el momento solo funciona con ese fps y tamaño
out = cv2.VideoWriter('ConvolutionVideoPrueba.mp4',fourcc, 20.0, (640,480))
operation = True

while operation:
    # Captura de un frame de video
    ret, frame = cap.read()
    # Aplicacion de filtros sobre un mismo frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(gray, (5,5),0)
    canny = cv2.Canny(gauss,50,150)
    (contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contornos,-1,(0,0,255), 2)
    # Frame guardado en archivo output
    out.write(frame)
    # Muestra de video con filtros en tiempo real
    cv2.imshow("Contornos",frame)

    # Fin de ciclo si se presiona SPACEBAR
    if cv2.waitKey(1) & 0xFF == ord(' '):
        operation = False

# Cerrar captura de video
cap.release()
# Cerrar archivo de output
out.release()
# Cerrar todas las ventanas creadas por el programa
cv2.destroyAllWindow()