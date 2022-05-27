#Check Switch status
# May 27th 2022

from machine import Pin
import time

#SW1 is connected to GPI018
SW1 = 18

sw1 = Pin(SW1, Pin.IN)

while True:
    print(sw1.value())
    time.sleep(1)