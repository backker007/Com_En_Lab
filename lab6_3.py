import RPi.GPIO as GPIO
import time
SW =22
LED=18
count = 0
aaa=False
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)
try:
    while True:
        if GPIO.wait_for_edge(SW, GPIO.FALLING):
                count = count + 1
        if count%2!=0:
            GPIO.output(18,True)
            print("LED => on")
            #GPIO.output(18,True)
        else:
            GPIO.output(18,False)
            print("LED => off")
            #GPIO.output(18,False)
except KeyboardInterrupt:
 GPIO.cleanup()
print("\nBye…")
 

