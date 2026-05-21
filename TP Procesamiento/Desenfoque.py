import numpy as np
from PIL import Image
from PIL import ImageFilter

    #Cargamos la imagen
img1=Image.open(r"C:\Users\Vero\Desktop\Tp Procesamiento digital de imágenes\TP procesamiento digital de imágenes/desenfoqueJPG.jpg")

    #Creamos la funcion para desenfocar la imagen
def desenfocar_imagen(imagen, radio=float):
    """
    Esta función recibe como parámetro la imagen y devuelve la imagen desenfocada.
    La función recibe dos parámetros: la imagen y el radio del desenfoque. 
    El radio es un valor de tipo float que determina la cantidad de desenfoque que se aplicará 
    a la imagen.     
    """
    return imagen.filter(ImageFilter.GaussianBlur(radius=radio))
if __name__== "__main__":
    #ejecutamos la funcion con parametro radio=10
    imagen_blureada = desenfocar_imagen(img1, radio=10)
    imagen_blureada.show()

#documentacion de la funcion desenfocar_imagen
#https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html#module-PIL.ImageFilter