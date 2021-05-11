import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import glob
files = glob.glob("digits/*.jpg")
train = []
train_labels = []
for iii,f in enumerate(files):
    img = cv.imread(f)
    grayImage = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,thresImg = cv.threshold(grayImage,100,255,cv.THRESH_BINARY)
    num = np.array(thresImg)
    num_ = num.reshape(-1,20*40).astype(np.float32)
    #print(num_)
    train.append(num_[0])
    #print(thresImg)   
    f = f.replace("digits\\", "")
    tp = f.split(" ")
    #print(tp[0])
    train_labels.append( int(tp[0]) )
x = np.array(train)
y = np.array(train_labels)
knn = cv.ml.KNearest_create()
#print(train[0])
knn.train(x,cv.ml.ROW_SAMPLE,y)    

img3 = cv.imread('digits/7 p49.jpg')
gray3 = cv.cvtColor(img3,cv.COLOR_BGR2GRAY)
num3 = np.array(gray3);
num3_ = num3.reshape(-1,20*40).astype(np.float32)
ret, result, neighbours ,dist = knn.findNearest(num3_,k=5)
print(result)