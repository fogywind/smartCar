#!/usr/bin/python
#coding=utf-8

import os
import voiceControl
import car
#import soundDetect
import time
import RPi.GPIO as GPIO

#定义声音传感器接口
Sensor = 16
LED = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Sensor, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
i=0

while True:

    detect = GPIO.input(Sensor)
    print(detect)


    if detect == 0:
        GPIO.output(LED, GPIO.HIGH)

        print('请说3秒话....')
        #调用arecord录3秒单声道16bit16k采样test.wav

        os.system('arecord -d 3 -r 16000 -f S16_LE test.wav')
        print ('稍等..')
        #调用百度语音识别
        a = voiceControl.voiceRecognize()
        if a != 1:
            print a
            if a.find(u'前')>= 0:
                car.forward(2)
                print 1
            elif a.find(u'后') >= 0:
                car.backward(2)
                print 2
            elif a.find(u'左') >= 0:
                car.turnLeft()
                print 3
            elif a.find(u'右') >= 0:
                car.turnRight()
                print 4
            elif a.find(u'掉头') >= 0:
                car.turnRight()
                car.turnRight()
                print 5
            else:
                print '我不知道你在说什么'
        else:
            print'识别错误'
        GPIO.output(LED, GPIO.LOW)
    else:
        i = i+1
        print(i)
        print ('nothing')
        time.sleep(0.1)







