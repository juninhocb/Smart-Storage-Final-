import cv2
import numpy as np

etiqueta = cv2.imread('teste.JPEG', 1)

cv2.namedWindow('Teste Open CV')
cv2.imshow('Teste Open CV', etiqueta)
cv2.waitKey()
