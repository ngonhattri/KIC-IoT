#Red LED turn on if sw1 is on
# May 27th 2022

import re
from machine import Pin
import time

# Red LED is connected to GPI016
RED = 16

# Red LED is connected to GPI05
GREEN = 5

#SW1 is connected to GPI018
SW1 = 18

#SW2 is connected to GPI019
SW2 = 19

# Create output pin
red = Pin(RED, Pin.OUT)
green = Pin(GREEN, Pin.OUT)

# Create input in
sw1 = Pin(SW1, Pin.IN)
sw2 = Pin(SW2, Pin.IN)

#Create FLag
swflag_red = 0

while True:
    status1 = sw1.value()
    status2 = sw2.value()
    if status1 == 0:
        swflag_red += 1
        if swflag_red == 20:
            red.on()
        print("SW1 ON")
    else:
        red.off()
    if status2 == 0:
        green.on()
        print("SW2 ON")
    else: 
        green.off()
    time.sleep(0.2)