import network
import socket
import sys
import time
from machine import Pin

# Default port number for WWW
PORT = 80

RED = 16

red = Pin(RED, Pin.OUT)

# Make HTTP header and HTML contents
html = """
HTTP/1.0 200 OK
Server: ESP32 HTTP Server
Content-type: text/html; charset=utf-8

<!DOCTYPE html>
<html>
  <head><title>ESP32 web server</title>
  <body>
    <h1>Welcome to ESP32 web server</h1>
      <form method="GET" acthon="#">
      <div>
          <input type="submit" name="switch" value="ON">
      </div>
      <div>
          <input type="submit" name="switch" value="OFF">
      </div>
      </form>
  </body>
</html>
"""
# Check WiFi connection and print IP address if connected
wlan = network.WLAN(network.STA_IF)
if wlan.isconnected():
  print(wlan.ifconfig())
else:
  print("Connect WiFi first.")
  exit(-1)

try:
  # Make socket as 's'
  s = socket.socket()

  # Would like to re-use the same socket address even it is already in use.
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  # 0.0.0.0 means any IP addresses given to ESP32 WiFi interface
  addr = ('0.0.0.0', PORT)

  # Assign IP address and Port
  s.bind(addr)

  # Only 1 conncection is acceptable
  s.listen(1)

  print("Waiting for connection...")

  while True:
    cl, addr = s.accept()
    print("Connected from", addr)
    
    # Print HTTP request from client
    buff = cl.recv(512)
    # Convert bytes to strings
    buff = buff.decode("utf-8")
    if len(buff) > 0:
      print("----- Client sent followings ------")
      print("----------\n")
    
    # Check which button was pressed
    if buff.find("/?switch=ON") == 4:
      red.on()
      print("ON was pressed.")

    if buff.find("/?switch=OFF") == 4:
      red.off()
      print("OFF was pressed.")


    cl.sendall(html)
    cl.close()
    print("Connection closed and waiting for next connection")

# Close socket if CTRL-C is press
except KeyboardInterrupt:
  s.close()