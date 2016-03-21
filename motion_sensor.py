import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(3, GPIO.OUT)

while True:
    i=GPIO.input(11)
    if i==0:
        print "No Intruders",i
        GPIO.output(3,0) # Turn OFF LEAD
        time.sleep(0.1)
    elif i==1:           # When output from motion sesnor is HIGH
        print "INTRUDER DETECTED",i
        GPIO.output(3,1) # Turn ON LED
        time.sleep(0.1)
