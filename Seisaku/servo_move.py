from machine import PWM, Pin
import time

# Servo motor is connecte to GPIO12
SERVO_PIN = 12

# PWM frequency is 50Hz
FREQ = 50

# Make servo instance
servo = PWM(Pin(SERVO_PIN), freq = FREQ)

def servocontrol(d):
    print("Duty:", d)
    servo.duty(d)
    time.sleep(1)

try:
    while True:
        # 117/1023 = 11% -> 90 degrees
        pwmduty = 117
        servocontrol(pwmduty)

        # neutral position (center)
        # 77/1023 = 7.5% -> 0 degree
        pwmduty = 77
        servocontrol(pwmduty)

        # 52/1023 = 5% -> -90 degrees
        pwmduty = 35
        servocontrol(pwmduty)

        # neutral position
        pwmduty = 77
        servocontrol(pwmduty)
        
except KeyboardInterrupt:
    print("Finished.")
    # set neutral position
    servo.duty(77)