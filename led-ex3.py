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



def ledonoff(stt):
    if stt == "ON":
        red.on()
    elif stt == "OFF":
        red.off()

try:
    while True:
        stt = input()
        ledonoff(stt)
        
except KeyboardInterrupt:
    red.off()
    yellow.off()
    green.off()