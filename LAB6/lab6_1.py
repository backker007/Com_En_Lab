import RPi.GPIO as GPIO
import time
LED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)
try:
    while True :
        GPIO.output (LED, True)
        time.sleep(0.1)
        GPIO.output(LED, False)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBye…")
