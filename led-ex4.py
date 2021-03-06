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
    color = input("input color:")
    if stt == "on":
        if color == "red":
            red.on()
        elif color == "green":
            green.on()
        elif color == "yellow":
            yellow.on()
    elif stt == "off":
        if color == "red":
            red.off()
        elif color == "green":
            green.off()
        elif color == "yellow":
            yellow.off()


try:
    while True:
        stt = input("input mode:")   
        ledonoff(stt)
        
except KeyboardInterrupt:
    red.off()