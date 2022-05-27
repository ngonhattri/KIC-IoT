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
        print("LED is on")
    if stt == "off":
        colored.off()
        print("LED is off")

try:
    while True:
        ledonoff("off", RED)
        time.sleep(0.5)
        ledonoff("on", RED)
        time.sleep(0.5)
        ledonoff("off", YELLOW)
        time.sleep(0.5)
        ledonoff("on", YELLOW)
        time.sleep(0.5)
        ledonoff("off", GREEN)
        time.sleep(0.5)
        ledonoff("on", GREEN)
        time.sleep(0.5)
except KeyboardInterrupt:
    ledonoff("off", RED)
    ledonoff("off", GREEN)
    ledonoff("off", YELLOW)