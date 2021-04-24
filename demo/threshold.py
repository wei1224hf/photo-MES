import cv2 as cv
import sys
img = cv.imread("test.png")
if img is None:
    sys.exit("Could not read the image.")
datas = [
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
for item in datas:
    ball = img[item[0]:item[1],item[2]:item[3]]
    ret,thresh1 = cv.threshold(ball,127,255,cv.THRESH_BINARY)
    cv.imshow("asdf"+str(item[0]), thresh1)


k = cv.waitKey(0)
if k == ord("1"):
    sys.exit(1)
