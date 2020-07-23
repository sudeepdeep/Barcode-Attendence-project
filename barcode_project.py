import cv2
import numpy as np
from pyzbar.pyzbar import decode
from datetime import datetime
import pandas as pd
roll_no = ['17HK1A0514','17HK1A0516']
            

cap = cv2.VideoCapture(0)

while True:

    ret,frame = cap.read()

    for barcode in  decode(frame):
        data = barcode.data.decode('UTF-8')
        if data in roll_no:
            text = "authorized"
            color = (0,255,0)
            with open(r"Desktop\Book1.csv",'r+') as f:
                data1 = f.readlines()
                my_data = []
                for datas in data1:
                    entries = datas.splitlines()
                    my_data.append(entries[0])
                    
                if data not in my_data:
                    noww = datetime.now()
                    formats = noww.strftime("%H:%M:%S")
                    f.writelines(f"\n{data},{formats}")
                    
        else:
            text = "un-authorized"
            color = (0,0,255)
        pts1 = np.array([barcode.polygon],np.int32)
        pts1 = pts1.reshape(-1,1,2)
        cv2.polylines(frame,[pts1],True,color,2)

        pts2 = barcode.rect
        cv2.putText(frame,text,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,color,2)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
