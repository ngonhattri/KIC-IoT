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


def ledonoff(stt, color):
    colored = Pin(color, Pin.OUT)
    if stt == "on":
        colored.on()
        time.sleep(0.5)
    if stt == "off":
        colored.on()
        time.sleep(0.5)


while True:
    ledonoff("off", RED)
    ledonoff("on", RED)
    ledonoff("off", YELLOW)
    ledonoff("on", YELLOW)
    ledonoff("off", GREEN)
    ledonoff("on", GREEN)