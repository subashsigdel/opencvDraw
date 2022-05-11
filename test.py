import math
import random
import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

xp, yp = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=1)
imgcanvas = np.zeros((400, 750, 3), np.uint8)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        pointIndex = lmList[8][0:2]

        cv2.circle(img, pointIndex, 15, (280, 0, 0), cv2.FILLED)
        if xp == 0 and yp == 0:
            xp, yp = pointIndex
        cv2.line(img, (xp, yp), pointIndex, (280, 0, 0), 15)
        cv2.line(imgcanvas, (xp, yp), pointIndex, (280, 0, 0), 15)
        xp, yp = pointIndex
    cv2.imshow("Image", img)
    cv2.imshow("canvas", imgcanvas)
    key = cv2.waitKey(1)
    if key == ord('r'):
        break
