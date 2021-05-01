import numpy as np
import cv2
from matplotlib import pyplot as plt

with np.load('knn_data.npz') as data:
    print(data.files)
    train = data['train']
    train_labels = data['train_labels']
    
    img = cv2.imread('digits.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
    img_test = cells[10][10]