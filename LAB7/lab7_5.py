import RPi.GPIO as GPIO
import time
import drivers
from time import sleep
display = drivers.Lcd()
display.lcd_clear()
SW1 = 27
SW2 = 17
lcd_position = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)
 
try:
  while True:
    if GPIO.event_detected(SW1):
        lcd_position += 1
        display.lcd_clear()
        display.lcd_display_string(" "*lcd_position + "Lab7",1)
        if(lcd_position==12):
            lcd_position=11
    elif GPIO.event_detected(SW2):
        lcd_position -= 1
        display.lcd_clear()
        display.lcd_display_string(" "*lcd_position + "Lab7",1)
        if(lcd_position==0):
         lcd_position=1
        #time.sleep(0.5)
   
except KeyboardInterrupt:
 GPIO.remove_event_detect(SW1)
 GPIO.remove_event_detect(SW2)
 display.lcd_clear()
 GPIO.cleanup()
 print("\nBye...")