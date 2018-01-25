import cv2
import numpy as np

#El 1 significa que queremos la imagen en BGR, y no en escala de grises
img = cv2.imread('circles.png',1)

#convertir nuestra imagen BGR en una imagen HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#El "dtype = np.uint8" simplemente significa que tendrá el tipo de datos un entero de 8 bits
lower_range = np.array([108, 100, 100], dtype=np.uint8)
upper_range = np.array([128, 255, 255], dtype=np.uint8)

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow('mask', mask)
cv2.imshow('image', img)

while (1):
    k = cv2.waitKey(0)
    if (k == 27):
        break

cv2.destroyAllWindows()

"""


cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([1, 100, 100], dtype=np.uint8)
    upper_blue = np.array([21, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()

"""


