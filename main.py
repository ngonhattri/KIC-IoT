from machine import Pin
import dht
import time

SENSOR = 21

# GPI016
RED = 16

#GPI017
YELLOW = 17

#GPI05
GREEN = 5

red = Pin(RED, Pin.OUT)
yellow = Pin(YELLOW, Pin.OUT)
green = Pin(GREEN, Pin.OUT)

# Make instance as 'd'
d = dht.DHT11(Pin(SENSOR))

def discomfort_index(T, H):
    res = 0.81*T+0.01*H*( 0.99*T-14.3 )+46.3
    return res

while True:
    d.measure()
    temperature = d.temperature()
    humidity = d.humidity()
    discomfort = discomfort_index(temperature, humidity)
    print("temperature: "+str(temperature)+"oC AND humidity: "+str(humidity) +"%")
    print("discomfort index: "+str(discomfort))
    if discomfort < 70:
        red.off()
        yellow.off()
        green.on()
    elif discomfort > 80:
        yellow.off()
        green.off()
        red.on()

    else:
        red.off()
        green.off()
        yellow.on()

    time.sleep(1)
    