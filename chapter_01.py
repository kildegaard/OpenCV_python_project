import cv2
import time
import numpy as np
print('Package imported')

# Leer imágenes
# img = cv2.imread('./resources/lena.png')

# cv2.imshow('Output', img)
# cv2.waitKey(1000)


# Leer videos y resize

# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture("resources/video_01.mp4")
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Result", img)
#
#     # time.sleep(1/60)
#
#     # Estas lineas añaden el delay (17 es 60 frames aprox, 1000ms/60) y la posibilidad de quitar con 'q'
#     if cv2.waitKey(17) & 0xFF == ord('q'):
#         break

# Uso de la webcam

# # 0 es para la webcam, otros números es por si tenés más cámaras
# cap = cv2.VideoCapture(0)
#
# # Los settings tienen códigos. 3 es para width y 4 es para height
# cap.set(3, 640)
# cap.set(4, 480)
#
# # También hay para el brillo:
# cap.set(10, 50)
# while True:
#     success, img = cap.read()
#     cv2.imshow("Webcam", img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# Convertir a grises una imagen

img = cv2.imread('./resources/lena.png')

# función para convertir colores
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Imagen en grises', img_gray)
# cv2.waitKey(1000)

# Le podemos agregar gaussian blur!

img_blur = cv2.GaussianBlur(img_gray, ksize=(7, 7), sigmaX=0)
# cv2.imshow('Imagen con blureo con 7', img_blur)

img_blur = cv2.GaussianBlur(img_gray, ksize=(15, 15), sigmaX=0)
# cv2.imshow('Imagen con blureo con 15', img_blur)

# cv2.waitKey(0)

# Ahora vamos a jugar con EDGE DETECTOR

img_canny = cv2.Canny(img, 150, 150)
cv2.imshow('Detectando bordes', img_canny)

# cv2.waitKey(0)

# Los bordes que detecta los podemos modificar con los argumentos.
# Estos bordes los podemos engrosar ("DILATE") o afinar ("ERODE")

kernel = np.ones(shape=(5, 5), dtype=np.uint8)

img_dilatada = cv2.dilate(img_canny, kernel=kernel, iterations=1)
img_eroded = cv2.erode(img_dilatada, kernel=kernel, iterations=1)

cv2.imshow('Imagen dilatada', img_dilatada)
cv2.imshow('Imagen erosionada', img_eroded)

cv2.waitKey(0)