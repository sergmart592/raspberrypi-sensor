import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)

while True:
    i=GPIO.input(3)    # Reading output of IR sensor
    if i==0:
        print "OBSTACLE DETECTED ", i
        time.sleep(0.1)
    else:
        print "NO OBSTACLE"
