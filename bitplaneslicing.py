import cv2
import numpy as np
from matplotlib import pyplot as plt3

img = cv2.imread('grayscaleImage.png',0)


imgs = [255 * ((img& (1<<i)) >>i) for i in range(8)]
for i in range(8):
    plt3.imshow(imgs[i],cmap='gray')
    plt3.show()

cv2.imwrite('bsp_1.jpg',imgs[0])
cv2.imwrite('bsp_2.jpg',imgs[1])
cv2.imwrite('bsp_3.jpg',imgs[2])
cv2.imwrite('bsp_4.jpg',imgs[3])
cv2.imwrite('bsp_5.jpg',imgs[4])
cv2.imwrite('bsp_6.jpg',imgs[5])
cv2.imwrite('bsp_7.jpg',imgs[6])
cv2.imwrite('bsp_8.jpg',imgs[7])



