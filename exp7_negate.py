import cv2
img = cv2.imread("./sample.jpg")
cv2.imshow("Pic",img)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_not = cv2.bitwise_not(img1)
cv2.imshow("Invert1",img_not)
cv2.waitKey(0)
cv2.destroyAllWindows()