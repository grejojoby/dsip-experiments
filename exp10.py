import cv2
import numpy as np
image = cv2.imread('sample.jpg')

kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)

cv2.imshow('Original', image)
cv2.imshow('Identity', identity)

cv2.waitKey()
cv2.imwrite('identity.jpg', identity)
cv2.destroyAllWindows()

median = cv2.medianBlur(src=image, ksize=15)

cv2.imshow('Original', image)
cv2.imshow('Median Blurred', median)
    
cv2.waitKey()
cv2.imwrite('median_blur.jpg', median)
cv2.destroyAllWindows()