import cv2
import numpy as np

def _dr1(img1):
    img1[img1 == 255] = 254
    img1=np.log(img1+ 1)
    return img1

def _dr(frame, c):
    return (c * frame).astype(np.uint8)

def chipka(bdr, gdr, rdr):
    q = []
    for i, j, k in zip(bdr, gdr, rdr):
        q.append(list(zip(i, j, k)))
    return np.array(q).astype(np.uint8)

img1 = cv2.imread('grayscaleImage.png')
b, g, r = img1[:, :, 0], img1[:, :, 1], img1[:, :, 2]
bdr1, gdr1, rdr1 = map(lambda x: _dr1(x), (b, g, r))
c = 40
bdr, gdr, rdr = map(lambda x: _dr(x, c), (bdr1, gdr1, rdr1))
res = chipka(bdr, gdr, rdr)
jo=cv2.imwrite('grayscaleImage_hdr.jpg', res)