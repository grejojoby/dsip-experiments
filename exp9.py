from __future__ import print_function
import cv2 as cv
import argparse
parser = argparse.ArgumentParser(description='Histogram Processing - DSIP Exp 9')
parser.add_argument('--input', help='Path to input image.', default='grayscaleImage.png')
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))

src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
dst = cv.equalizeHist(src)
cv.imshow('Source image', src)
cv.imshow('Equalized Image', dst)
cv.waitKey()
