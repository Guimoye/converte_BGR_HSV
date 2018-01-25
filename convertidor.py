import sys
import numpy as np
import cv2

#R= 237 G =28 B=36
blue    = 204
green   = 72
red     = 63

#el orden está en BGR no en RBG
color = np.uint8([[[blue, green, red]]])
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

hue = hsv_color[0][0][0]

print("Lower bound is :"),
print("[" + str(hue - 10) + ", 100, 100]\n")

print("Upper bound is :"),
print("[" + str(hue + 10) + ", 255, 255]")