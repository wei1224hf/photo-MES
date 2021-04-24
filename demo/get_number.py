import cv2 
import sys
import numpy as np
import pytesseract
from imutils.perspective import four_point_transform
from imutils import contours
import imutils



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


'''水平投影'''
def getHProjection(image):
    hProjection = np.zeros(image.shape,np.uint8)
    #图像高与宽
    (h,w)=image.shape
    #长度与图像高度一致的数组
    h_ = [0]*h
    #循环统计每一行白色像素的个数
    for y in range(h):
        for x in range(w):
            if image[y,x] == 255:
                h_[y]+=1
    #绘制水平投影图像
    for y in range(h):
        for x in range(h_[y]):
            hProjection[y,x] = 255
    cv2.imshow('hProjection2',hProjection)
 
    return h_
 
def getVProjection(image):
    vProjection = np.zeros(image.shape,np.uint8);
    #图像高与宽
    (h,w) = image.shape
    #长度与图像宽度一致的数组
    w_ = [0]*w
    #循环统计每一列白色像素的个数
    for x in range(w):
        for y in range(h):
            if image[y,x] == 255:
                w_[x]+=1
    #绘制垂直平投影图像
    for x in range(w):
        for y in range(h-w_[x],h):
            vProjection[y,x] = 255
    cv2.imshow('vProjection',vProjection)
    return w_
 
if __name__ == "__main__":
    #print(sys.argv[0])
    #print(sys.argv[2])
    arg_area = sys.argv[2].split(',');
    areas = []
    idx = 0
    area = []
    for ss in arg_area:
        area.append(int(ss))
        idx = idx+1
        if (idx==4):
            idx = 0            
            areas.append(area)
            area = []
    origineImage = cv2.imread("G:\\project\\photo-MES\\demo\\"+sys.argv[1])
    origineImage = cv2.cvtColor(origineImage,cv2.COLOR_BGR2GRAY)
    if origineImage is None:
        sys.exit("Could not read the image.")
'''        
    datas = [
    #[314,341,544,686],
    [88,127,168,369 ],
    [94,124,639,743 ],
    [142,174,621,742 ],
    [142,176,155,204 ],
    [141,176,322,366 ],
    [137,177,482,525 ],
    [361,393,167,369 ],
    [360,394,648,740 ],
    [406,434,661,744 ],
    [482,511,655,744 ],
    [517,546,653,744 ]
    ]
'''
    item = areas[0]
    print(item)
    #for item in datas:
    ball = origineImage[item[0]:item[1],item[2]:item[3]]
    ret,thresh1 = cv2.threshold(ball,127,255,cv2.THRESH_BINARY)
    
    cv2.waitKey(0)  
    cv2.bitwise_not(thresh1, thresh1)
    #cv2.imshow("as111df"+str(item[0]), thresh1)
  
    #thresh = cv2.threshold(thresh1, 0, 255,
    #    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
    #cv2.cvtColor(ball, cv2.COLOR_BGR2GRAY);
    #thresh = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
    dst=cv2.GaussianBlur(thresh1,(1,3),5)

    ret,dst = cv2.threshold(dst,127,255,cv2.THRESH_BINARY)
    #cv2.imshow("asdf"+str(item[0]), dst)
    cv2.waitKey(0)    
    contoursx, hierarchyx = cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #print(contoursx);
    #cv2.imshow("asdf"+str(item[0]), hierarchyx)
    #cnts = imutils.grab_contours(contoursx)
    #print(cnts)
    #cv2.waitKey(0)
    digitCnts = []
    # loop over the digit area candidates
    for c in contoursx:
        # compute the bounding box of the contour
        (x, y, w, h) = cv2.boundingRect(c)
        #print(x,y,w,h)
        # if the contour is sufficiently large, it must be a digit
        #if w >= 15 and (h >= 30 and h <= 40):
        digitCnts.append(c)  
    #print(len(contoursx))
    digitCnts = contours.sort_contours(digitCnts, method="left-to-right")[0]
    digits = [];
    #print(digits);
    idx = 0
    for c in digitCnts:
        # extract the digit ROI
        (x, y, w, h) = cv2.boundingRect(c)
        roi = dst[y:y + h, x:x + w]
        #cv2.imshow("bbbbbb", roi)
                
        if w < 10:
            digits.append(1)
            idx += 1
            continue
        idx += 1

        cv2.waitKey(0)
        # compute the width and height of each of the 7 segments
        # we are going to examine
        (roiH, roiW) = roi.shape
        (dW, dH) = (int(roiW * 0.25), int(roiH * 0.15))
        #print("roiH,roiW,dW,dH",roiH,roiW,dW,dH)
        dHC = int(roiH * 0.05)
        if(dHC==0):
            dHC=1
        
        # define the set of 7 segments
        segments = [
            ((0, 0), (w, dH)),	# top
            ((0, 0), (dW, h // 2)),	# top-left
            ((w - dW, 0), (w, h // 2)),	# top-right
            ((0, (h // 2) - dHC) , (w, (h // 2) + dHC)), # center
            ((0, h // 2), (dW, h)),	# bottom-left
            ((w - dW, h // 2), (w, h)),	# bottom-right
            ((0, h - dH), (w, h))	# bottom
        ]
        on = [0] * len(segments)     
        # loop over the segments
        for (i, ((xA, yA), (xB, yB))) in enumerate(segments):
            # extract the segment ROI, count the total number of
            # thresholded pixels in the segment, and then compute
            # the area of the segment
            #print("yA,yB, xA,xB",yA,yB, xA,xB)
            segROI = roi[yA:yB, xA:xB]

            total = cv2.countNonZero(segROI)
            area = (xB - xA) * (yB - yA)
            # if the total number of non-zero pixels is greater than
            # 50% of the area, mark the segment as "on"
            if (area>0) and (total / float(area)) > 0.5:
                on[i]= 1
                #cv2.imshow("bbbbbb", segROI)
                #cv2.waitKey(0)
            #print("on",on)
        # lookup the digit and draw it on the image
        digit = DIGITS_LOOKUP[tuple(on)]
        digits.append(digit)
        #cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 1)
        #cv2.putText(output, str(digit), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)        
    print("digits",digits)
    #text = pytesseract.image_to_string(ball,lang="eng")
    #print(text)
    #cv2.waitKey(0)
'''
    W = getVProjection(ball)
    print(W)
    cv2.imshow("asdf"+str(item[0]), thresh1)
    cv2.waitKey(0)
    image = cv2.cvtColor(origineImage,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',image)
    # 将图片二值化
    retval, img = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('binary',img)
    #图像高与宽
    (h,w)=img.shape
    Position = []
    #水平投影
    H = getHProjection(img)
 
    start = 0
    H_Start = []
    H_End = []
    #根据水平投影获取垂直分割位置
    for i in range(len(H)):
        if H[i] > 0 and start ==0:
            H_Start.append(i)
            start = 1
        if H[i] <= 0 and start == 1:
            H_End.append(i)
            start = 0
    #分割行，分割之后再进行列分割并保存分割位置
    for i in range(len(H_Start)):
        #获取行图像
        cropImg = img[H_Start[i]:H_End[i], 0:w]
        #cv2.imshow('cropImg',cropImg)
        #对行图像进行垂直投影
        W = getVProjection(cropImg)
        Wstart = 0
        Wend = 0
        W_Start = 0
        W_End = 0
        for j in range(len(W)):
            if W[j] > 0 and Wstart ==0:
                W_Start =j
                Wstart = 1
                Wend=0
            if W[j] <= 0 and Wstart == 1:
                W_End =j
                Wstart = 0
                Wend=1
            if Wend == 1:
                Position.append([W_Start,H_Start[i],W_End,H_End[i]])
                Wend =0
    #根据确定的位置分割字符
    for m in range(len(Position)):
        cv2.rectangle(origineImage, (Position[m][0],Position[m][1]), (Position[m][2],Position[m][3]), (0 ,229 ,238), 1)
    cv2.imshow('image',origineImage)
    cv2.waitKey(0)
'''

