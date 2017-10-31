#!/usr/bin/python

import cv2.cv as cv
import time


capture = cv.CaptureFromCAM(0)
cv.SetCaptureProperty(capture,3,360)
cv.SetCaptureProperty(capture,3,240)

while True:
    img = cv.QueryFrame(capture)

    cv.Smooth(img,img,cv.CV_BLUR,3)
    hue_img = cv.CreateImage(cv.GetSize(img),8,3)
    cv.CvtColor(img,hue_img,cv.CV_BGR2HSV)

    threshold_img = cv.CreateImage(cv.GetSize(hue_img),8,1)
    cv.InRangeS(hue_img,(38,120,60),(75,255,255),threshold_img)

    
    cv.ShowImage("color tracking", img)
    cv.ShowImage("threshold",threshold_img)
    if cv.WaitKey(10) == 27:
        break
cv.DestroyAllWindows()
