#Red LED turn on if sw1 is on
# May 27th 2022
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
swflag_green = 0

while True:
    stt_red = sw1.value()
    stt_green = sw2.value()

    if stt_red == 0:
        time.sleep(0.1)
        swflag_red += 1
        print(swflag_red)
        if swflag_red == 2:
            red.on()
            print("SW1 ON")
            time.sleep(3)
            red.off()
            swflag_red = 0
    else:
        swflag_red = 0
        red.off()

    if stt_green == 0:
        time.sleep(0.1)
        swflag_green += 1
        print(swflag_green)

        if swflag_green == 2:
            green.on()
            print("SW2 ON")
            time.sleep(3)

            green.off()
            swflag_red = 0

    else:
        swflag_green = 0
        green.off()