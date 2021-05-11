from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse

#读取原图
img = cv.imread("demo.jpg")
img_original = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#AB线性锐化,使得4个mark点突出
#e1 = cv.getTickCount()
sabs = cv.convertScaleAbs(img_original, alpha=20, beta=0)
res = cv.bitwise_not(sabs,sabs)
#e2 = cv.getTickCount()
#t = (e2 - e1)/cv.getTickFrequency()

#对原图做4个mark点定位
res = cv.medianBlur(res,5)
#e3 = cv.getTickCount()
#t = (e3 - e2)/cv.getTickFrequency()
#寻找4个圆心
circles = cv.HoughCircles(res, cv.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 15, 22)
#e4 = cv.getTickCount()
#t = (e4 - e3)/cv.getTickFrequency()
#画圆需要整数坐标                  
circles = np.uint16(np.around(circles))
#对算出来的4个mark点求中心点,同时画圆
c = [0,0]
for i in circles[0,:]:
    c[0]=i[0]+c[0]
    c[1]=i[1]+c[1]
    cv.circle(img,(i[0],i[1]),i[2],(0,255,0),1)
    cv.circle(img,(i[0],i[1]),2,(0,0,255),3)
c[0]=c[0]/4
c[1]=c[1]/4
c = np.uint16(np.around(c))
cv.circle(img,(c[0],c[1]),2,(0,0,255),3)
#算出左上角跟左侧直线,因为要做倾斜角计算,要所以要转换为int型
lt = [0,0]
lb = [0,0]
rt = [0,0]
rb = [0,0]
for i in circles[0,:]:
    if(i[0]<c[0] and i[1]<c[1]):
        lt[0]=int(i[0])
        lt[1]=int(i[1])
    if(i[0]<c[0] and i[1]>c[1]):
        lb[0]=int(i[0])
        lb[1]=int(i[1])
    if(i[0]>c[0] and i[1]<c[1]):
        rt[0]=int(i[0])
        rt[1]=int(i[1])
    if(i[0]>c[0] and i[1]>c[1]):
        rb[0]=int(i[0])
        rb[1]=int(i[1])        
cv.line(img,(lt[0],lt[1]),(lb[0],lb[1]),(0,0,255),2)
cv.line(img,(rt[0],rt[1]),(rb[0],rb[1]),(0,0,255),2)
#计算出斜率及角度
k1 = (-1)*float((lb[0]-lt[0])/(lb[1]-lt[1]))
angle1 = np.arctan(k1)* 57.29577
k2 = (-1)*float((rb[0]-rt[0])/(rb[1]-rt[1]))
angle2 = np.arctan(k2)* 57.29577
angle = (angle1+angle2)/2
#中心为圆心做旋转
rot_mat = cv.getRotationMatrix2D((c[0],c[1]), angle, 1.0)
(h, w) = img.shape[:2]
rotated = cv.warpAffine(sabs, rot_mat, (w, h))
#cv.imshow("orgin", img)
cv.imwrite('G:/project/photo-MES/demo/imgwithlines.jpg',img)
cv.imwrite('G:/project/photo-MES/demo/demo_2.jpg',rotated)


