from machine import Pin
import dht
import time

SENSOR = 21

# Make instance as 'd'
d = dht.DHT11(Pin(SENSOR))

while True:
    d.measure()
    temperature = d.temperature()
    humidity = d.humidity()
    print(temperature, humidity)
    time.sleep(1)