import numpy as np
import cv2 as cv
from time import sleep

#原图读取
img = cv.imread("demo.jpg")
grayImage = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#AB线性锐化,使得4个mark点突出
sabs = cv.convertScaleAbs(grayImage, alpha=20, beta=0)
cv.imwrite('G:/project/photo-MES/demo/sabs.jpg',sabs)
res = cv.bitwise_not(sabs,sabs)
#对原图做4个mark点定位
res = cv.medianBlur(res,5)
cv.imwrite('G:/project/photo-MES/demo/res.jpg',res)
#寻找4个圆心
circles = cv.HoughCircles(res, cv.HOUGH_GRADIENT, 1, res.shape[0]/8, np.array([]), 100, 20, 15, 22)
print(len(circles[0]))
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
#cv.imwrite('G:/project/photo-MES/demo/imgwithcycles.jpg',img)
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
#cv.imwrite('G:/project/photo-MES/demo/imgwithlines.jpg',img)
#cv.imwrite('G:/project/photo-MES/demo/rot_mat.jpg',rotated)

#膨胀化
dilImg = cv.dilate(rotated,  np.ones((3, 3), dtype=np.uint8), 1)
#腐蚀化
erosImg = cv.erode(dilImg,  np.ones((3, 3), dtype=np.uint8), iterations=1)
#二值化
ret,thresImg = cv.threshold(erosImg,100,255,cv.THRESH_BINARY)
cv.imwrite('G:/project/photo-MES/demo/erosImg.jpg',erosImg)
(h, w) = thresImg.shape[:2]
h2 = int(h*0.9)
w2 = int(w*0.9)
imgCut = thresImg[int((h-h2)/2):h2, int((w-w2)/2):w2]
cv.imwrite('G:/project/photo-MES/demo/imgCut.jpg',imgCut)
contoursx, hierarchyx = cv.findContours(imgCut,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
#print(contoursx);

for iii,c in enumerate(contoursx):
    (x, y, w, h) = cv.boundingRect(c)
    roi = imgCut[y:y + h, x:x + w]   
    cv.imwrite('G:/project/photo-MES/demo/p1/p'+str(iii)+'.jpg',roi)

    if(h<19 or h>40):continue
    if(w<2 or w>45):continue
    if(w>30 and w<45 ):
        rp1 = roi[:h,:20]
        rp2 = roi[:h,21:w]
        
        (h1, w1) = rp1.shape[:2]
        if(w1>20):w1 = 20
        (h2, w2) = rp2.shape[:2]
        if(w2>20):w2 = 20
        print("h2,w2",h2,w2)
        mask = np.zeros((40, 20), dtype=roi.dtype)
        mask[int((40-h1)/2):int((40-h1)/2)+h1, int((20-w1)/2):int((20-w1)/2)+w1] = rp1[:h1,:w1]
        cv.imwrite('G:/project/photo-MES/demo/p/p'+str(iii)+'a.jpg',mask)
        
        mask = np.zeros((40, 20), dtype=roi.dtype)
        mask[int((40-h2)/2):int((40-h2)/2)+h2, int((20-w2)/2):int((20-w2)/2)+w2] = rp2[:h2,:w2]
        cv.imwrite('G:/project/photo-MES/demo/p/p'+str(iii)+'b.jpg',mask)        
    else:    
        if(w>20):w=20
        mask = np.zeros((40, 20), dtype=roi.dtype)
        mask[int((40-h)/2):int((40-h)/2)+h, int((20-w)/2):int((20-w)/2)+w] = imgCut[y:y + h, x:x + w]   
        cv.imwrite('G:/project/photo-MES/demo/p/p'+str(iii)+'.jpg',mask)