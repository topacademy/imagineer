#!/usr/bin/python

from PiMotor import Sensor
us = Sensor("ULTRASONIC", 10)

while True:
    us.sonicCheck()
    if us.Triggered:
        print("Sonic detected obtstruction")

    
    
        


