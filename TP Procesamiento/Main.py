import numpy as np
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from Brillo import aumentar_brillo
from Contorno import resaltar_contorno
from Desenfoque import desenfocar_imagen  

#Cargamos la imagen
imgMain= Image.open(r"C:\Users\Vero\Desktop\TP procesamiento digital de imágenes\TP procesamiento digital de imágenes/main.jpg")

#Llamamos a la funcion para aumentar el brillo de la imagen
img_brillante2= aumentar_brillo(imgMain, 2)
img_brillante2.show()

#Llamamos a la funcion para resaltar el contorno de la imagen
img_contorno2= resaltar_contorno(imgMain)
img_contorno2.show()

#Llamamos a la funcion para desenfocar la imagen
img_desenfocada2= desenfocar_imagen(imgMain, radio=3)   
img_desenfocada2.show()