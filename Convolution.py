import numpy as np
import cv2

imOrigin = cv2.imread("monedas.jpg")
cv2.imshow("Original", imOrigin)

grey = cv2.cvtColor(imOrigin,cv2.COLOR_BGR2GRAY)

gauss = cv2.GaussianBlur(grey, (5,5),0)

cv2.imshow("Suavizado", gauss)

canny = cv2.Canny(gauss,50,150)

cv2.imshow("canny", canny)

(contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("He encontrado {} objetos". format(len(contornos)))

cv2.drawContours(imOrigin,contornos,-1,(0,0,255), 2)

cv2.imshow("Contornos", imOrigin)

cv2.waitKey(0)