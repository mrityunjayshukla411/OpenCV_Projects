import cv2
import time
import numpy as np
import math
import sys
sys.path.insert(0, '/mjs/programming/openCV/OpenCV_Projects/modules')
import HandTrackingModule as htm

wCam, hCam = 640, 480 # size of window
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
    
detector = htm.handDetector(detectionCon= 0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw= False)
    if len(lmList) != 0:
        print(lmList[4],lmList[8])
        
        x1, y1 = lmList[4][1] ,lmList[4][2]
        x2, y2 = lmList[8][1] ,lmList[8][2]
        cx, cy = (x1 + x2) //2 , (y1 + y2) //2 
        
        cv2.circle(img, (x1,y1), 15 , (25,127,99), cv2.FILLED)
        cv2.circle(img, (x2,y2), 15 , (25,127,99), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (255,7,8),3)
        cv2.circle(img, (cx,cy), 15 , (255,127,99), cv2.FILLED)
        
        length = math.hypot(x2-x1,y2-y1)
        print(length)
        if length <= 40:
            cv2.circle(img, (cx,cy), 15 ,(123,43,123), cv2.FILLED)
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,f'FPS: {int(fps)}',(40,70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 127), 3)
    
    cv2.imshow('Img', img)
    k = cv2.waitKey(1) 
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()