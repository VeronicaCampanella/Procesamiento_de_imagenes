import numpy as np
from PIL import Image
from PIL import ImageEnhance
#

    
    #Cargamos la imagen
img2=Image.open(r"C:\Users\Vero\Desktop\TP procesamiento digital de imágenes\TP procesamiento digital de imágenes\brillo.jpg") 

    #creamos la funcion para aumentar el brillo de la imagen
def aumentar_brillo(imagen, factor):
    """ 
    La función fue creada para aumentar el brillo de una imagen utilizando el modulo ImageEnhance.
    La función recibe dos parámetros: la imagen y el factor de aumento del brillo.
    El factor es un argumento que no es definido previamente,
    sino que es un valor que será instanciado luego para ser llamado y modificado desde otro lugar del código."""
    enhancer = ImageEnhance.Brightness(imagen)
    return enhancer.enhance(factor)
if __name__ == "__main__":
    #instancia del objeto img
    img_brillante = aumentar_brillo(img2, 1.5)
    img_brillante.show()

#documentacion de la funcion aumentar_brillo
#https://pillow.readthedocs.io/en/stable/reference/ImageEnhance.html#module-PIL.ImageEnhance


