import cv2
import numpy as np
image=cv2.imread('/home/rino/Documents/tugas/bunga.jpg')
cv2.imshow('ori',image)
kernel_sharpening=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
sharpend=cv2.filter2D(image, -1,kernel_sharpening)
cv2.imshow('sharpening_image',sharpend)
cv2.waitKey(0)
cv2.destroyAllWindows()
