import RPi.GPIO as GPIO
import time
SW = 22
#GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# กำหนดขา GPIO ของ LED RGB
RED_PIN = 3
GREEN_PIN = 2
BLUE_PIN = 4
# กำหนดขา GPIO ของปุ่มสวิทซ์
#SWITCH_PIN = 23
# ตั้งค่า GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT) 
GPIO.setup(BLUE_PIN, GPIO.OUT)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# ตั้งค่า PWM สำหรับการควบคุมสี
#int2rgb = lambda x: ((x >> 16)&0xff,(x>>8)&0xff,(x)&0xff)
red_pwm = GPIO.PWM(RED_PIN, 100)
green_pwm = GPIO.PWM(GREEN_PIN, 100)
blue_pwm = GPIO.PWM(BLUE_PIN, 100)

# สตาร์ท PWM
red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

colors = [
    (0, 0, 0),
    (0, 0, 100),    
    (0, 100, 0),    
    (0, 100, 100), 
    (100, 0, 0), 
    (100, 0, 100),    
    (100, 100, 0),    
    (100, 100, 100)    
    ]
    #เพิ่มสีต่อไปตามต้องการ
current_color_index = 0
try :
         while True:
             switch_state = GPIO.input(SW)
             if switch_state == GPIO.LOW:  # ตรวจสอบสถานะปุ่ม (ถ้าปุ่มถูกกด)
                current_color = colors[current_color_index]
                red_pwm.ChangeDutyCycle(current_color[0])
                green_pwm.ChangeDutyCycle(current_color[1])
                blue_pwm.ChangeDutyCycle(current_color[2])
                print(f"LED RGB => ({current_color[0]}, {current_color[1]}, {current_color[2]})")
                time.sleep(1)  # รอเพื่อป้องกันการกดปุ่มซ้ำ
                current_color_index = (current_color_index + 1) % len(colors)
except KeyboardInterrupt:
      GPIO.cleanup()
print("\nBye…")