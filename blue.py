import cv2
import numpy as np
import imutils

img = cv2.imread('/home/rino/Documents/tugas/kancing.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([109,49,49])
upper_range = np.array([131,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow('ori', img)
cv2.imshow('masked', mask)

while(True):
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
                break

cv2.destroyAllowWindows()
