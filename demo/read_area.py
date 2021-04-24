import cv2 as cv
import sys
img = cv.imread("test.png")
if img is None:
    sys.exit("Could not read the image.")
ball = img[64:86,119:269]
cv.imshow("Display window", ball)
k = cv.waitKey(0)
if k == ord("1"):
    sys.exit(1)
