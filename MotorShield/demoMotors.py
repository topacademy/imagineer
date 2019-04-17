#!/usr/bin/python

import PiMotor
import time
#import RPi.GPIO as GPIO

#Name of Individual MOTORS 
m1 = PiMotor.Motor("MOTOR1",1)

##This segment drives the motors in the direction listed below:
## forward and reverse takes speed in percentage(0-100)

try:
    while True:
#-----------To Drive the Motors Forward------------# 
        print("Robot Moving Forward ")
        m1.forward(100)
        time.sleep(5)
#--------------------------------------------------#

#-----------To Drive the Motors backwards------------# 
        print("Robot Moving Backward ")
        m1.reverse(20)
        time.sleep(5)
#--------------------------------------------------#

#---------To Stop the Motor----------------------#
        print("Robot Stop ")
        m1.stop()
        time.sleep(5)
#-------------------------------------------------#

        
except KeyboardInterrupt:
    GPIO.cleanup()

    
