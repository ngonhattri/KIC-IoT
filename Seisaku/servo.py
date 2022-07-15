import time
from machine import Pin, PWM

# servo = PWM(Pin(13), freq=50)
# servo.duty(26)
# time.sleep_ms(1000)
# servo.duty(115)
# time.sleep_ms(1000)
# servo.duty(77)

servo = Pin(13, Pin.OUT)
pwm = PWM(servo)
# pwm
# class Servo():
#   def __init__(self, pinNum, min=40, max=115, freq=50):
#     self.min = min
#     self.max = max
#     self.sv = PWM(Pin(pinNum))
#     self.sv.freq(freq)
#     self.nowduty = 0
    
#   def Angle(self, ang):
#     self.nowduty = self.map(ang, 0, 180, self.min, self.max)
#     self.sv.duty(self.nowduty)
    
#   def Enable(self):
#     self.sv.deinit()
    
#   def map(self, x, imin, imax, omin, omax):
#     buf = (x - imin) * (omax - omin) / (imax - imin) + omin
#     if buf < omin:
#       buf = omin
#     if buf > omax:
#       buf = omax
#     return int(buf)
  
# S = Servo(12, 30, 120)
# ANG = [0, 180, 90, 0, 120, 30, 0]
# for i in ANG:
#   S.Angle(i)
#   time.sleep(1)