# Blink 3 LEDs connected to GPI016, 17,  5
# Turn off the LED when CTRL-C pressed
# May 13 2022 チー

from machine import Pin
import time

# GPI016
RED = 16

#GPI017
YELLOW = 17

#GPI05
GREEN = 5

#SW1 is connected to GPI018
SW1 = 18

#SW2 is connected to GPI019
SW2 = 19

# Create input in
sw1 = Pin(SW1, Pin.IN)
sw2 = Pin(SW2, Pin.IN)

red = Pin(RED, Pin.OUT)
yellow = Pin(YELLOW, Pin.OUT)
green = Pin(GREEN, Pin.OUT)

led = [ (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]

swFlag = 0

def ledonoff(n):
    global swFlag
    if swFlag < 7:
        l = led[n]      
        g = l[0] #green
        y = l[1] #yellow
        r = l[2] #red
        if g == 0: 
            green.off()
        if y == 0:
            yellow.off()
        if r == 0:
            red.off()
        if g == 1:
            green.on()
        if y == 1:
            yellow.on()
        if r == 1:
            red.on()

def ledreset():
    global swFlag
    red.off()
    green.off()
    yellow.off()

    swFlag = 0

try:
    while True:
        stt1 = sw1.value()
        if stt1 == 0:
            ledonoff(swFlag)
            swFlag += 1
            time.sleep(0.5)
        
        stt2 = sw2.value()
        if stt2 == 0:
            ledreset()

except KeyboardInterrupt:
    red.off()
    yellow.off()
    green.off()

