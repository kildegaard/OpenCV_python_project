import cv2
import time
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

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    cv2.imshow("Webcam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break