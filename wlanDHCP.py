# Connect WiFi network and get information
# Disconnect Wifi after 60 seconds

import binascii
import network
import time

# mywifi.py contain SSID and PASS information
# You shoud put this file into ESP32
import mywifi

# Wait time to disconnect Wifi
TIMEUP = 60

# SSID & PASS are defined in mywifi.py file
SSID = mywifi.SSID
PASS = mywifi.PASS

# Make wlan instance
wlan = network.WLAN(network.STA_IF)

# Activate Wifi interface
wlan.active(True)
time.sleep(1)

if not wlan.isconnected():
    print("Connecting Wifi.", end='')
    wlan.connect(SSID, PASS)
    time.sleep_ms(100)

    # wait until WiFi is connected
    while not wlan.isconnected():
        print(".", end='')
        time.sleep_ms(200)
        pass
    print()

print("Connected WiFi")


# Get WIfi radio wave signal strength
rssi = wlan.status('rssi')

# Get MAC address and decode
macaddr = binascii.hexlify(wlan.config('mac'),':').decode()

# Get network information and print it
myip, mynetmask, myroute, mydns, = wlan.ifconfig()
wifiinfo = (myip, myroute, mydns, rssi, macaddr)
print("My IP: %s\nGateway: %s\nDNS: %s\nRSSI: %.1f\nMAC ADD: %s" %wifiinfo)

# Wait for TIMEUP seconds
for n in range(TIMEUP):
    time.sleep(1)
    # insert new line every 10 dots
    if n % 10 == 0:
        print()
    print(".", end='')

# disconnect wifi
wlan.disconnect()
print('\nTime up!')
print('Disconnected.')
