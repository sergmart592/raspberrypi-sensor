import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # use board pin numbers
# define pin #7 as input pin
pin = 7
GPIO.setup(pin, GPIO.IN) 

while 1:
    if GPIO.input(pin) == GPIO.LOW:
        print "SOUND DETECTED!!!!"
        time.sleep(1)
    #else:
    #    print "NO SOUND"
    #    time.sleep(1)
    #    GPIO.setup(7,GPIO.OUT)
