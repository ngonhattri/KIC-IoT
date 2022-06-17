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
swflag = 0
ledFlag = False
while True:
    stt_red = sw1.value()
    stt_green = sw2.value()
    if stt_red == 0:
        time.sleep(0.1)
        swflag += 1
        print(swflag)
        if (swflag == 20) & (ledFlag == False):
            red.on()
            print("SW1 ON")
            swflag = 0
            ledFlag = True

        elif (swflag == 20) & (ledFlag == True):
            red.off()
            print("SW1 OFF")
            swflag_red = 0
            ledFlag = False
        
    elif stt_green == 0:
        time.sleep(0.1)
        swflag += 1
        print(swflag)
        if (swflag == 20) & (ledFlag == False):
            green.on()
            print("SW2 ON")
            swflag = 0
            ledFlag = True

        elif (swflag == 20) & (ledFlag == True):
            green.off()
            print("SW2 OFF")
            swflag = 0
            ledFlag = False
        
    else:
        swflag = 0
        
