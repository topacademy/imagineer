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

ir1 = Sensor("IR1",0)
ir2 = Sensor("IR2",0)

while True:
    ir1.trigger()
    if ir1.Triggered:
        print("No Line Detected - IR1")
    else:
        print("Black Line Detected - IR1")
    ir2.trigger()
    if ir2.Triggered:
        print("No Line Detected - IR2")
    else:
        print("Black Line Detected - IR2") 

#    except KeyboardInterrupt:
#        GPIO.cleanup()
