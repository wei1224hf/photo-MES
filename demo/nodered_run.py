import cv2 
import sys
import numpy as np
#import pytesseract
from imutils.perspective import four_point_transform
from imutils import contours
import imutils


#断码屏
#  1
#2   3
#  4
#5   6
#  7
DIGITS_LOOKUP = {
	(1, 1, 1, 0, 1, 1, 1): 0,
	(0, 0, 1, 0, 0, 1, 0): 1,
	(1, 0, 1, 1, 1, 0, 1): 2,
	(1, 0, 1, 1, 0, 1, 1): 3,
	(0, 1, 1, 1, 0, 1, 0): 4,
	(1, 1, 0, 1, 0, 1, 1): 5,
	(1, 1, 0, 1, 1, 1, 1): 6,
	(1, 0, 1, 0, 0, 1, 0): 7,
	(1, 1, 1, 1, 1, 1, 1): 8,
	(1, 1, 1, 1, 0, 1, 1): 9
}
 
if __name__ == "__main__":
    arg_area = sys.argv[2].split(',');
    #arg_area = ('652,684,571,747,abc,700,731,576,747,ee').split(',')
    areas = []
    idx = 0
    area = []
    names = []
    for ss in arg_area:
        if ss.isdigit():
            area.append(int(ss))
        else:
            names.append(ss)
        idx = idx+1
        if (idx==5):
            idx = 0            
            areas.append(area)
            area = []
    origineImage = cv2.imread("G:\\project\\photo-MES\\demo\\"+sys.argv[1])
    if origineImage is None:
        sys.exit("Could not read the image.")
    origineImage = cv2.cvtColor(origineImage,cv2.COLOR_BGR2GRAY)  
    print("[",end='',sep='')    
    for ii,item in enumerate(areas):
        #挖取区域内的图片
        ball = origineImage[item[0]:item[1],item[2]:item[3]]
        ret,thresh1 = cv2.threshold(ball,127,255,cv2.THRESH_BINARY)
          
        cv2.bitwise_not(thresh1, thresh1)
        
      
        #纵向高斯模糊数字,使断码连成一片
        dst=cv2.GaussianBlur(thresh1,(1,3),5)
        dst = cv2.erode(dst,np.ones((1,2),np.uint8))
        ret,dst = cv2.threshold(dst,127,255,cv2.THRESH_BINARY)
        #cv2.imshow("ccccc", dst)
        k = cv2.waitKey(0)
        
        #如果只是判断黑点
        if names[ii].find("__")!=-1:
            contoursy, hierarchyy = cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            for c in contoursy:
                (x, y, w, h) = cv2.boundingRect(c)
                #roi = dst[y:y + h, x:x + w]
                #cv2.imshow("asdfasdfasdf", roi)
                #print("w,h",w,h)
                
                if w >= 15 and h >= 15 :
                    print("[\"",names[ii]+"\",",1,"],",end='',sep='')
        #如果要判断黑点
        else:
        
            #得到所有数字
            contoursx, hierarchyx = cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

            digitCnts = []
            for iii,c in enumerate(contoursx):
                (x, y, w, h) = cv2.boundingRect(c)
                roi = dst[y:y + h, x:x + w]
                #print(x,y,w,h)
                # if the contour is sufficiently large, it must be a digit
                #if w >= 15 and (h >= 30 and h <= 40):
                digitCnts.append(c)  
            if len(digitCnts)>0:
                digitCnts = contours.sort_contours(digitCnts, method="left-to-right")[0]
                digits = [];
                idx = 0
                for iiii,c in enumerate(digitCnts):
                    (x, y, w, h) = cv2.boundingRect(c)
                    #挖取单个数字
                    roi = dst[y:y + h, x:x + w]
                    #cv2.imshow("ccccc", roi)
                    #cv2.waitKey(0)
                    #数字非常宅,必定是 1
                    if w < 5:
                        digits.append(1)
                        idx += 1
                        continue
                    idx += 1
                    
                    (roiH, roiW) = roi.shape
                    (dW, dH) = (int(roiW * 0.25), int(roiH * 0.15))
                    #print("roiH,roiW,dW,dH",roiH,roiW,dW,dH)
                    dHC = int(roiH * 0.05)
                    if(dHC==0):
                        dHC=1
                    
                    #定义断码位置高度宽度
                    segments = [
                        ((0+1, 0), (w-1, dH)),	# top
                        ((0, 0+1), (dW, (h-2) // 2)),	# top-left
                        ((w - dW, 0+1), (w, (h-2) // 2)),	# top-right
                        ((0+1, (h // 2) - dHC) , (w-1, (h // 2) + dHC)), # center
                        ((0, (h+4) // 2), (dW, (h-4))),	# bottom-left
                        ((w - dW, (h+4) // 2), (w, (h-4))),	# bottom-right
                        ((0+1, h - dH), (w-1, h))	# bottom
                    ]
                    on = [0] * len(segments)     
                    #判断每个断码是否点亮
                    for (i, ((xA, yA), (xB, yB))) in enumerate(segments):
                        #print("yA,yB, xA,xB",yA,yB, xA,xB)
                        segROI = roi[yA:yB, xA:xB]
                        #cv2.imshow("bbbbbb"+str(i), segROI)
                        #cv2.waitKey(0)
                        total = cv2.countNonZero(segROI)
                        area = (xB - xA) * (yB - yA)

                            
                        if (area>0) and (total / float(area)) > 0.45:
                            on[i]= 1
                        else:
                            foobar = 1
                            #print(area,total)
                        #print("on",on)
                    try:
                        digit = DIGITS_LOOKUP[tuple(on)]
                        digits.append(digit)   
                    except :
                        foobar = 1
                        #print('------------',names[ii])
                    
                    
                print("[\"",names[ii]+"\",",digits,"],",end='',sep='')
    print("XXX",end='',sep='')
    print("]",end='',sep='')
