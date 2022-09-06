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

def servo_value(degree):
    return int((degree * 9.5 / 180 + 2.5) * 65535 / 100)
try:
    while True:
        #reading = sensor_adc.read_u16()
        servo.duty_u16(servo_value(0))
        print(servo_value(0))
        time.sleep(1)
        servo.duty_u16(servo_value(45))
        print(servo_value(45))
        time.sleep(1)
        servo.duty_u16(servo_value(90))
        print(servo_value(90))
        time.sleep(1)
        servo.duty_u16(servo_value(135))
        print(servo_value(135))
        time.sleep(1)
        servo.duty_u16(servo_value(180))
        print(servo_value(180))
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Finished.")
    # set neutral position
    servo.duty_u16(servo_value(0))