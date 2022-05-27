#Blink LED connected to GPI016
# May 13 2022 チー
import machine
import time

# red LED is connected to GPI016
LED = 16

# Create ouput pin as 'led'
led = machine.Pin(LED, machine.Pin.OUT)

while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)