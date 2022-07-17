# Servo motor control sample program
# Jul. 10th T.Kawamoto

from machine import PWM, Pin
import time

# Servo motor is connecte to GPIO12
SERVO_PIN = 18

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
        # 103/1023 = 10% -> 90 degrees
        #pwmduty = 103
        pwmduty = 115

        # Move to 0 degree position
        servocontrol(pwmduty)


        # neutral position (center)
        # 77/1023 = 7.5% -> 0 degree
        pwmduty = 77
        servocontrol(pwmduty)

        # 52/1023 = 5% -> -90 degrees
        #wmduty = 52
        pwmduty = 40
        servocontrol(pwmduty)

        # neutral position
        pwmduty = 77
        servocontrol(pwmduty)
            
except KeyboardInterrupt:
    print("Finished.")
    # set neutral position
    servo.duty(77)