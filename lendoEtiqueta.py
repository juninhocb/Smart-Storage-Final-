import pytesseract as ocr
from PIL import Image
import PIL
import pytesseract
#import cv2
import numpy as np
from stringFind import userFind



def lerEtiqueta(img):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    imgLida = pytesseract.image_to_string(Image.open(img))

    #etiqueta = cv2.imread(img, 1)

    usuarioComBarraN = userFind(imgLida)
    
    usuario = usuarioComBarraN.rstrip()


    ## prints e testes
    #cv2.namedWindow('EtiquetaLida')
    #cv2.imshow('EtiquetaLida', etiqueta)
    #cv2.waitKey()

    #print(imgLida)
    #print(usuario)
        
    return usuario


    

#detectaNome = imgLida[20:ultimoCaracter]

#print(detectaNome)
      

    
    