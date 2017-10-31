#!/usr/bin/python
#coding=utf-8
import RPi.GPIO as GPIO
import time

#设置GPIO模式
GPIO.setmode(GPIO.BOARD)

#设置in1到in4接口,具体接口具体分析

IN1 = 11
IN2 = 12
IN3 = 13
IN4 = 15

#初始化接口

def init():
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

#前进
def forward(movingTime):
    init()
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(movingTime)
    close()

#后退
def backward(movingTime):
    init()
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    time.sleep(movingTime)
    close()

#左转
def turnLeft():
    init()
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(0.56)
    close()

#右转
def turnRight():
    init()
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    time.sleep(0.55)
    close()

#清端口
def close():
    GPIO.cleanup()

#-------------主程序-----------------------

#init()          #初始化
#sforward(1)
#backward(1)
#turnRight()     #前进10秒
#turnLeft()
