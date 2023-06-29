import cv2
import numpy as np
from pyzbar.pyzbar import decode




#img = cv2.imread('hello.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('DataList.txt') as f:
    DataList = f.read().splitlines()

while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        

        if myData in DataList:
            Output= 'Authorized'
            mycolor = (0,255,0)
        else:
            Output= "Un-Authorized"
            mycolor = (0,0,255)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,mycolor,5)
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,mycolor,2)



    cv2.imshow('Result',img)
    cv2.waitKey(1)
 