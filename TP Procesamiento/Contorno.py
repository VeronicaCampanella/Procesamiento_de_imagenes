import numpy as np
from PIL import Image
from PIL import ImageFilter


#Cargar la imagen
img3=Image.open(r"C:\Users\Vero\Desktop\Tp Procesamiento digital de imágenes\TP procesamiento digital de imágenes\contorno.jpg")
    #Vamos a crear una función que resalte el contorno de la imagen utilizando el filtro de contorno con ImageFilter.CONTOUR
#
def resaltar_contorno(imagen):
    """
    Esta función recibe como parámetro la imagen y devuelve la imagen con el contorno resaltado.
    Esta función devuelve la imagen modificada por el modulo ImageFilter.
    con su método CONTOUR, que resalta los bordes de la imagen.
    """
    return imagen.filter(ImageFilter.CONTOUR)
if __name__== "__main__":
    #Vamos a aumentar la nitidez de la imagen utilizando el filtro de contorno con ImageFilter.CONTOUR
    imagen_contorno = resaltar_contorno(img3)
    imagen_contorno.show()