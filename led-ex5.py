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

red = Pin(RED, Pin.OUT)
yellow = Pin(YELLOW, Pin.OUT)
green = Pin(GREEN, Pin.OUT)

led = [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]

try:
    while True:
        for l in led:
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
            time.sleep(0.5)
        
except KeyboardInterrupt:
    red.off()
    yellow.off()
    green.off()

