import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import glob
from imutils import contours
import imutils
import sys
import os

fpath = 'G:/project/mes-ne/photo-MES/demo/produce/'

def KNN():
    files = glob.glob(fpath+"../digits/*.jpg")

    train = []
    train_labels = []
    for iii,f in enumerate(files):
        img = cv.imread(f)
        grayImage = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        ret,thresImg = cv.threshold(grayImage,100,255,cv.THRESH_BINARY)
        num = np.array(thresImg)
        num_ = num.reshape(-1,20*40).astype(np.float32)
        train.append(num_[0]) 
        g = f.split("\\")        
        tp = g[1].split(" ")
        train_labels.append( int(tp[0]) )
    x = np.array(train)
    y = np.array(train_labels)
    knn = cv.ml.KNearest_create()
    #print(train[0])
    knn.train(x,cv.ml.ROW_SAMPLE,y)   
    return knn
    
def recognize(imgCut,knn,idx=1):
    results = []
    #膨胀化
    dilImg = cv.dilate(imgCut,  np.ones((2, 2), dtype=np.uint8), 1)
    #腐蚀化
    erosImg = cv.erode(dilImg,  np.ones((1, 1), dtype=np.uint8), iterations=1)
    #二值化
    ret,dst = cv.threshold(erosImg,100,255,cv.THRESH_BINARY)
    cv.imwrite(fpath+'dst.jpg',dst)
    contoursx, hierarchyx = cv.findContours(dst,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    contoursOrderd = []
    for i1,c in enumerate(contoursx):
        (x, y, w, h) = cv.boundingRect(c)
        roi = dst[y:y + h, x:x + w]
        if w >= 2 and (h >= 20 and h <= 40):
            contoursOrderd.append(c)  
    if len(contoursOrderd)>0:
        contoursOrderd = contours.sort_contours(contoursOrderd, method="left-to-right")[0]
        for i2,c in enumerate(contoursOrderd):
            (x, y, w, h) = cv.boundingRect(c)
            roi = dst[y:y + h, x:x + w]   

            if(h<19):continue
            if(h>40):h=40
            if(w<2 or w>45):continue
            if(w>30 and w<45 ):
                rp1 = roi[:h,:20]
                rp2 = roi[:h,21:w]
                
                (h1, w1) = rp1.shape[:2]
                if(w1>20):w1 = 20
                (h2, w2) = rp2.shape[:2]
                if(w2>20):w2 = 20
                mask = np.zeros((40, 20), dtype=roi.dtype)
                mask[int((40-h1)/2):int((40-h1)/2)+h1, int((20-w1)/2):int((20-w1)/2)+w1] = rp1[:h1,:w1]

                num3 = np.array(mask);
                num3_ = num3.reshape(-1,20*40).astype(np.float32)
                ret, result, neighbours ,dist = knn.findNearest(num3_,k=5)
                results.append(result[0][0])
                cv.imwrite(fpath+'knn/'+str(idx)+'_'+str(i2)+' '+str(result[0][0])+'a.jpg',mask)
                
                mask = np.zeros((40, 20), dtype=roi.dtype)
                mask[int((40-h2)/2):int((40-h2)/2)+h2, int((20-w2)/2):int((20-w2)/2)+w2] = rp2[:h2,:w2]

                num3 = np.array(mask);
                num3_ = num3.reshape(-1,20*40).astype(np.float32)
                ret, result, neighbours ,dist = knn.findNearest(num3_,k=5)
                results.append(result[0][0])           
                cv.imwrite(fpath+'knn/'+str(idx)+'_'+str(i2)+' '+str(result[0][0])+'b.jpg',mask)
            else:    
                if(w>20):w=20
                mask = np.zeros((40, 20), dtype=roi.dtype)
                mask[int((40-h)/2):int((40-h)/2)+h, int((20-w)/2):int((20-w)/2)+w] = dst[y:y + h, x:x + w]   
                
                num3 = np.array(mask);
                num3_ = num3.reshape(-1,20*40).astype(np.float32)
                ret, result, neighbours ,dist = knn.findNearest(num3_,k=5)
                results.append(result[0][0])
                cv.imwrite(fpath+'knn/'+str(idx)+'_'+str(i2)+' '+str(result[0][0])+'.jpg',mask)
    rt = ''
    for i4,r1 in enumerate(results):
        rt = rt + str(int(r1))
    return rt

def readPhotoAndRotate(img):
    #读取原图
    img_original = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite(fpath+'img_original.jpg',img_original)
    #AB线性锐化,使得4个mark点突出
    sabs = cv.convertScaleAbs(img_original, alpha=5, beta=10)
    #sabs = cv.convertScaleAbs(img_original, alpha=20, beta=10)
    res = cv.bitwise_not(sabs,sabs)
    cv.imwrite(fpath+'res.jpg',res)
    template = cv.imread(fpath+'../template.jpg',0)
    w, h = template.shape[::-1]

    tlps = cv.matchTemplate(res,template,cv.TM_CCOEFF_NORMED    )
    threshold = 0.75
    c = [0,0]
    points = []
    loc = np.where( tlps >= threshold)

    for pt in zip(*loc[::-1]):
        #cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        ptt = [int(pt[0] + w/2),int(pt[1] + h/2)]
        containd = 0
        for pt2 in points:
            if ((pt2[0] - ptt[0])*(pt2[0] - ptt[0]) + (pt2[1] - ptt[1])*(pt2[1] - ptt[1])) < 40:
                containd = 1
                continue
        if(containd==0):
            points.append(ptt)
            cv.circle(img,(ptt[0],ptt[1]),20,(0,0,255),1)
            cv.circle(img,(ptt[0],ptt[1]),2,(0,0,255),2)
            c[0]=int(pt[0] + w/2)+c[0]
            c[1]=int(pt[1] + h/2)+c[1]
    c[0]=int(c[0]/4)
    c[1]=int(c[1]/4)
    cv.circle(img,(c[0],c[1]),2,(0,0,255),3)
    
    #算出左上角跟左侧直线,因为要做倾斜角计算,要所以要转换为int型
    lt = [0,0]
    lb = [0,0]
    rt = [0,0]
    rb = [0,0]
    for pt in zip(*loc[::-1]):
        i = [int(pt[0] + w/2), int(pt[1] + h/2)]
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
    
    cv.imwrite(fpath+'template.jpg',img)

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
    
    return rotated
    
def deleteOld():
    directory = fpath+""
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".jpg")]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)
        
    directory = fpath+"knn/"
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".jpg")]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)        

if __name__ == "__main__":
    deleteOld()
    arg_areas = sys.argv[1]
    #print("arg_areas",arg_areas)
    #arg_areas = '203,252,1063,1136 ,"state-2", 260,343,374,777 ,"time_start" , 260,321,1208,1339 ,"user1",355,426,540,623 ,"class-3"'
    arg_areas = arg_areas.replace(" ","")
    arg_areas = arg_areas.replace("\"","")
    arg_areas = arg_areas.split(',')

    areas = []
    area = []
    names = []
    for ss in arg_areas:
        if ss.isdigit():
            area.append(int(ss))
        else:
            names.append(ss)          
            areas.append(area)
            area = []
          
    img = cv.imread(fpath+"../photo.jpg")
    rotated = readPhotoAndRotate(img)
    knn = KNN()
    
    ct = [0,0]
    ouputs = []
    for i1,c in enumerate(areas):
        name = names[i1]
        c[0] = int(c[0])
        c[1] = int(c[1])
        c[2] = int(c[2])
        c[3] = int(c[3])
        if name == 'box':
            ct = [ int((c[3]+c[2])/2), int((c[1]+c[0])/2) ]
            cv.circle(rotated,(ct[0],ct[1]),2,(0,255,255),3)
            cv.imwrite(fpath+'rotated.jpg',rotated)
        elif (name == 'state-1' or name == 'state-2' or name == 'state-3' or name == 'state-4' or name == 'class-1' or name == 'class-2' or name == 'class-3'):
            area1 = [ c[0]-ct[1],c[1]-ct[1],c[2]-ct[0],c[3]-ct[0] ]   
            area1_img = rotated[area1[0]+ct[1]:area1[1]+ct[1],area1[2]+ct[0]:area1[3]+ct[0]]  
            n_white_pix = np.sum(area1_img >= 120)  

            if(n_white_pix>200):
                ouputs.append([1,name])
            cv.imwrite(fpath+str(i1)+'.jpg',area1_img)            
        else:
            area1 = [ c[0]-ct[1],c[1]-ct[1],c[2]-ct[0],c[3]-ct[0] ]   
            area1_img = rotated[area1[0]+ct[1]:area1[1]+ct[1],area1[2]+ct[0]:area1[3]+ct[0]]
            
            data = recognize(area1_img,knn,i1)
            ouputs.append([data,name])
            cv.imwrite(fpath+str(i1)+'_'+name+'_'+data+'.jpg',area1_img)            

    print(ouputs,end='',sep='')

    
'''
    arr = [[154,1855,180,1381 ,"box"],[260,343,374,777 ,"t"]]
    ab = arr[0]
    pt1 = arr[1]
    ct = [ int((ab[3]+ab[2])/2), int((ab[1]+ab[0])/2) ]
    area1 = [ pt1[0]-ct[1],pt1[1]-ct[1],pt1[2]-ct[0],pt1[3]-ct[0] ]    

    img = cv.imread("demo.jpg")
    rotated = readPhotoAndRotate(img)
    area1_img = rotated[area1[0]+c[1]:area1[1]+c[1],area1[2]+c[0]:area1[3]+c[0]]
    knn = KNN()
    data = recognize(area1_img,knn)


    cv.imwrite('G:/project/photo-MES/demo/o/area1_img.jpg',area1_img)

'''

