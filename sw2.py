#Red LED turn on if sw1 is on
# May 27th 2022

from machine import Pin
import time

# Red LED is connected to GPI016
RED = 16

#SW1 is connected to GPI018
SW1 = 18

# Create output pin as 'led'
led = Pin(RED, Pin.OUT)

# Create input in as 'sw1'
sw1 = Pin(SW1, Pin.IN)

while True:
    status = sw1.value()
    if status == 0:
        led.on()
        print("SW1 ON")
    else: 
        led.off()
    time.sleep(0.2)