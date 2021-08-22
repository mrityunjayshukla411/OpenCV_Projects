import cv2
import mediapipe as mp
import time
import pyautogui as pt

import sys
sys.path.insert(0, '/mjs/programming/openCV/OpenCV_Projects/modules')
import HandTrackingModule as htm


pTime = 0 
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=False, trackPoint=8)
    if len(lmList) != 0:
        print(lmList[8])
        cv2.line(img, (0,200),(630,200),(255,32,78),6)
        cv2.circle(img, (lmList[8][1], lmList[8][2]), 15, (255, 0, 0), cv2.FILLED)
        if(lmList[8][2] > 200):
            pt.press('up')

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(
        img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3
    )

    cv2.imshow("Image", img)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
