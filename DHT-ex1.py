from machine import Pin
import dht
import time

SENSOR = 21

# Make instance as 'd'
d = dht.DHT11(Pin(SENSOR))

def discomfort_index(T, H):
    res = 0.81*T+0.01*H*( 0.99*T-14.3 )+46.3
    print("discomfort index: "+str(res))

while True:
    d.measure()
    temperature = d.temperature()
    humidity = d.humidity()
    print("temperature: "+str(temperature)+"oC AND humidity: "+str(humidity) +"%")
    discomfort_index(temperature, humidity)
    time.sleep(1)
    