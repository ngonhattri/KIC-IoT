
from machine import Pin
# from plyer import battery

import time

SENSOR = 21
# GPI016
RED = 16
#GPI017
YELLOW = 17
#GPI05
GREEN = 5

red = Pin(RED, Pin.OUT)
yellow = Pin(YELLOW, Pin.OUT)
green = Pin(GREEN, Pin.OUT)


# バッテリーの状況
# status = battery.get_state()
print(status)

while True:
    if status < 70:
        green.on()
    elif status > 80:
        red.on()
    else:
        yellow.on()

    time.sleep(1)
    