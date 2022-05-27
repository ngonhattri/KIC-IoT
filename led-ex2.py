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

try:
    while True:
        green.on()
        time.sleep(2)
        green.off()
        time.sleep(0.1)

        yellow.on()
        time.sleep(2)        
        yellow.off()
        time.sleep(0.1)

        red.on()
        time.sleep(2)
        red.off()
        time.sleep(0.1)     
        
except KeyboardInterrupt:
    red.off()
    yellow.off()
    green.off()