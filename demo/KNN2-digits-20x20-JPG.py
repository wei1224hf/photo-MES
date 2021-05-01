import numpy as np
import cv2
from matplotlib import pyplot as plt

#读取样本图片
img = cv2.imread('digits.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#样本切分
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
#图片数字化
x = np.array(cells)
train = x[:,:100].reshape(-1,400).astype(np.float32) # Size = (2500,400)
#生成对应文字
k = np.arange(10)
train_labels = np.repeat(k,500)[:,np.newaxis]
test_labels = train_labels.copy()
#生成测试模型
knn = cv2.ml.KNearest_create()
knn.train(train,cv2.ml.ROW_SAMPLE,train_labels)
#读取图片
img3 = cv2.imread('3.jpg')
gray3 = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
cv2.imshow("ccccc1", gray3)
num3 = np.array(gray3);
num3_ = num3.reshape(-1,400).astype(np.float32)
ret, result, neighbours ,dist = knn.findNearest(num3_,k=5)
print(result)
k = cv2.waitKey(0) 