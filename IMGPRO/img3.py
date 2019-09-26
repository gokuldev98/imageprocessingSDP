import cv2
import numpy as np
import matplotlib.pyplot as plt

def to_canny(image):
    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,50,150)
    return canny

def region_of_interest(image):
    height=image.shape[0]
    triangle=[np.array([[200,height],[1100,height],[550,250]],dtype=np.int32)]
    mask=np.zeros_like(image)
    cv2.fillPoly(mask,triangle,255)#white triangle
    masked_image=cv2.bitwise_and(image,mask)
    return masked_image

image=cv2.imread('roadimage.jpg')
lane_image=np.copy(image)
canny=to_canny(lane_image)
cv2.imshow("region",region_of_interest(canny))
cv2.waitKey(0)
