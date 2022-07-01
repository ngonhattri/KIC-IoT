# Connect WiFi network using Static(Fixed) IP
# Jun 22th 2022 T.Kawamoto

import binascii
import network
import time
from machine import Pin

#GPI05
GREEN = 5
green = Pin(GREEN, Pin.OUT)

# mywifistatic.py contains several information related to network.
# You should put this file(mywifistatic.py) into ESP32
import mywifistatic

# These are defined in 'mywifistatic.py' file
SSID = mywifistatic.SSID
PASS = mywifistatic.PASS
MYHOSTNAME = mywifistatic.MYHOSTNAME
MYIP = mywifistatic.MYIP
MYNETMASK = mywifistatic.MYNETMASK
MYDNS = mywifistatic.MYDNS
MYGATEWAY = mywifistatic.MYGATEWAY

# This shuld be a tupple
MYNETINFO = (MYIP, MYNETMASK, MYGATEWAY, MYDNS)

# Make wlan instance as WiFi station
wlan = network.WLAN(network.STA_IF)

# Activate WiFi interface
wlan.active(True)
time.sleep(1)

# Set WiFi interface
wlan.ifconfig(MYNETINFO)

# If WiFi is not connected, try to connect it.
if not wlan.isconnected():
    print("Connecting WiFi.", end='')
    wlan.connect(SSID, PASS)
    time.sleep_ms(100)
    # wait until WiFi is connected
    while not wlan.isconnected():
        print(".", end='')
        green.on()
        time.sleep(0.1)
        green.off()
        time.sleep(0.1)
        pass
    print()

print("Connected WiFi")
green.on()

# Set hostname
wlan.config(dhcp_hostname=MYHOSTNAME)

# Get WiFi radio wave signal strength
rssi = wlan.status('rssi')

# Get hostname to check
hostname = wlan.config("dhcp_hostname")

# Get MAC address and decode
macaddr = binascii.hexlify(wlan.config('mac'),':').decode()

# Get network information and print it
myip, mynetmask, myroute, mydns = wlan.ifconfig()
wifiinfo = (myip, myroute, mydns, rssi, macaddr)
print("\nMy IP: %s\nGateway: %s\nDNS: %s\nRSSI: %.1f\nMACADDR: %s" % wifiinfo)
print("hostname:", hostname)
