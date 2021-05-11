from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse

alpha = 1.0
alpha_max = 500
beta = 0
beta_max = 200
gamma = 1.0
gamma_max = 200

def basicLinearTransform():
    res = cv.convertScaleAbs(img_original, alpha=alpha, beta=beta)
    img_corrected = cv.hconcat([img_original, res])
    cv.imshow("Brightness and contrast adjustments", img_corrected)

def gammaCorrection():
    ## [changing-contrast-brightness-gamma-correction]
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)

    res = cv.LUT(img_original, lookUpTable)
    ## [changing-contrast-brightness-gamma-correction]

    img_gamma_corrected = cv.hconcat([img_original, res])
    cv.imshow("Gamma correction", img_gamma_corrected)

def on_linear_transform_alpha_trackbar(val):
    global alpha
    alpha = val / 100
    basicLinearTransform()

def on_linear_transform_beta_trackbar(val):
    global beta
    beta = val - 100
    basicLinearTransform()

def on_gamma_correction_trackbar(val):
    global gamma
    gamma = val / 100
    gammaCorrection()



img_original = cv.imread("demo.jpg")
res = cv.convertScaleAbs(img_original, alpha=20, beta=0)
cv.imshow("Brightness and contrast adjustments", res)
cv.imwrite('G:/project/photo-MES/demo/demo_2.jpg',res)


cv.waitKey()
