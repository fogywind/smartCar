#coding: utf-8

import RPi.GPIO
import time

#二极管24
LED = 24
#声音传感器接23
Sensor = 23

flag = False #标注当前状态

RPi.GPIO.setmode(RPi.GPIO.BCM)

#指定23为输入模式
RPi.GPIO.setup(Sensor, RPi.GPIO.IN, pull_up_down = RPi.GPIO.PUD_UP)

#指定24为输出
RPi.GPIO.setup(LED, RPi.GPIO.OUT)

try:
    while True:
        #低电平为输出
        if (RPi.GPIO.input(Sensor) == 0):
            flag =not flag
            RPi.GPIO.output(LED, flag)
            time.sleep(0.5)
except KeyboardInterrupt:
    pass



RPi.GPIO.cleanup()
#lalala