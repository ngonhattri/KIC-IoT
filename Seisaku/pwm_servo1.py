from machine import PWM, Pin
import time

# Servo motor is connecte to GPIO12
SERVO_PIN = 12

# PWM frequency is 50Hz
FREQ = 50
 
# Make servo instance
servo = PWM(Pin(SERVO_PIN), freq = FREQ)

def servo_value(degree):
    return int((degree * 9.5 / 180 + 2.5) * 65535 / 100)


try:
  while True:
      # 0 degree　1.45ms
      # servo.duty_ns(int(1.45*10**6))
      servo.duty_u16(servo_value(0))
      print(servo_value(0))
      time.sleep(1)
      # 90 degrees 2.4ms
      # servo.duty_ns(int(2.4*10**6))
      servo.duty_u16(servo_value(90))
      time.sleep(1)
      
      # -90 degrees 0.5ms
      # servo.duty_ns(int(0.5*10**6))
      servo.duty_u16(servo_value(-90))
      time.sleep(1)
      
except KeyboardInterrupt:
  print("Finished.")
  # set neutral position
  servo.duty_ns(int(1.45*10**6))
