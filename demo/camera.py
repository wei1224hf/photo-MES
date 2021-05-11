import numpy as np
import cv2
from time import sleep
import socket

fpath = 'G:/project/mes-ne/photo-MES/demo/'

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
    
    
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                ret, frame = cap.read()
                #frame = rotateImage(frame,90)
                # Our operations on the frame come here
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                #cv2.imshow('frame',gray)
                gray = cv2.rotate(gray, cv2.ROTATE_90_CLOCKWISE)
                #ret,gray = cv2.threshold(gray,140,255,cv2.THRESH_BINARY)
                dim = (793, 1122)
                resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)
                #cv2.imshow('frame2',resized)                         
                cv2.imwrite(fpath+'photo.jpg',gray)
                my_str_as_bytes = str.encode('1')
                #conn.sendall(my_str_as_bytes)    

cap.release()
cv2.destroyAllWindows()