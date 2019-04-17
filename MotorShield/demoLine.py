import time
import sys
sys.path.append("/home/pi/MotorShield")
from PiMotor import Arrow
from PiMotor import Sensor
from PiMotor import Motor

m1 = Motor("MOTOR1",1)
m2 = Motor("MOTOR2",1)
m3 = Motor("MOTOR3",1)
m4 = Motor("MOTOR4",1)
us = Sensor("ULTRASONIC", 10)

ls1 = Sensor("IR1",0)
ls2 = Sensor("IR2",0)

while True:
    ls1.iRCheck()
    if ls1.Triggered:
        print("IR1 detected black line")
    ls2.iRCheck()
    if ls2.Triggered:
        print("IR2 detected black line")
    
    
        


