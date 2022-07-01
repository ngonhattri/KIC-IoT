# Scan Wifi network around ESP32

import network
import binascii
import   time

security = ['open', 'WEP', 'WPA-PSK', 'WPA2-PSK', 'WPA/WPA2-PSK']

# Make wlan instance as station
wlan = network.WLAN(network.STA_IF)

# Activate Wifi interface
wlan.active(True)

# Scan Wifi once and print it
wifilist = wlan.scan()
print(wifilist)

# Print details in 'wifilist'
for eachwifi in wifilist:
    print("----------")
    print("SSID:"+eachwifi[0].decode())
    print("BSSID:"+ binascii.hexlify(eachwifi[1],':').decode())
    print("Channel:"+str(eachwifi[2]))
    print("RSSI:"  + str(eachwifi[3]) )
    print("Security:" + security[eachwifi[4]])
    if eachwifi[5] == 0:
        print("Hidden: Visible")
    else:
        print("Hidden: invisible")

    time.sleep(1)
        