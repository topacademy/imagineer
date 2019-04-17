import sys
sys.path.append("/home/pi/MotorShield")
import time
from PiMotor import Motor
Motor("MOTOR1",1).forward(f,100)
time.sleep(5)
Motor("MOTOR1",1).reverse(r,100)
time.sleep(5)
Motor("MOTOR1",1).stop()
