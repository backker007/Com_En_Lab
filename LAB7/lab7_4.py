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
a = True
try:
  while a:
        if GPIO.event_detected(SW1):
            lcd_position += 1
            print(f"SW1 Pressed : {lcd_position}")
        elif GPIO.event_detected(SW2):
            a = False
            GPIO.remove_event_detect(SW1)
            GPIO.remove_event_detect(SW2)
            GPIO.cleanup()
            display.lcd_clear()
            print("\nBye...")
            time.sleep(0.5)
        if (lcd_position == 1):
            display.lcd_display_string("Danupohn   ", 1)
            display.lcd_display_string("1165104620398", 2)
            time.sleep(0.5)
        if (lcd_position == 2):
            display.lcd_display_string("Anuphong    ", 1)
            display.lcd_display_string("1165104006622", 2)
            time.sleep(0.5)
        if (lcd_position == 3):
            display.lcd_display_string("Chananchida    ", 1)
            display.lcd_display_string("1165104005905", 2)
            lcd_position = 0
            time.sleep(0.5)
       
   
       
except KeyboardInterrupt:
  GPIO.remove_event_detect(SW1)
  GPIO.remove_event_detect(SW2)
  GPIO.cleanup()
  display.lcd_clear()
  print("\nBye...")
 