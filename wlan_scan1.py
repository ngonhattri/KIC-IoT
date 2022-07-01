#Scan Wifi network around ESP32

import network
import time

# make wlan instance as station
wlan = network.WLAN(network.STA_IF)

# Activate Wifi interface
wlan.active(True)

# Scan 5 times every 1 sec
for n in range(5):
    print(wlan.scan())
    time.sleep(1)