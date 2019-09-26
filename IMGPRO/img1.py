import cv2
import numpy as np
# Load a color image in grayscale
image = cv2.imread('salah.jpg')
lane_image=np.copy(image)
gray=cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow('input',gray)
cv2.imshow("result",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
