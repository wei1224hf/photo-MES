import numpy as np
import cv2
from time import sleep


#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2048)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1536)

def rotateImage(image, angle):
    (x, y, col, row) = cv2.boundingRect(image)
    #row,col = image.shape
    center=tuple(np.array([row,col])/2)
    rot_mat = cv2.getRotationMatrix2D(center,angle,1.0)
    new_image = cv2.warpAffine(image, rot_mat, (col,row))
    return new_image

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #frame = rotateImage(frame,90)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame',gray)
    gray = cv2.rotate(gray, cv2.ROTATE_90_CLOCKWISE)
    #ret,gray = cv2.threshold(gray,140,255,cv2.THRESH_BINARY)
    dim = (793, 1122)
    resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow('frame2',resized)
    #sleep(0.1)
    cv2.waitKey(0)
             
    cv2.imwrite('G:/project/photo-MES/demo/demo.jpg',gray)
'''    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        if not cv2.imwrite('G:/project/photo-MES/demo/demo.jpg',dst2):
            raise Exception("Could not write image")
        cv2.waitKey(0)
        break
'''
# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()