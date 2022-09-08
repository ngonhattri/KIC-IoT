import network
import socket
# Default port number for WWW
PORT = 80
switch_state = "OFF"
# Make HTTP header and HTML contents
html = """
<!DOCTYPE html>
<html>
  <head>
  <meta charset="utf-8">
  <title>ESP32 web server</title>
  </head>
  <body>
    <h1>ESP32 switchbot</h1>
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
      print("ON was pressed.")

    if buff.find("/?switch=OFF") == 4:
      print("OFF was pressed.")

    cl.send('HTTP/1.1 200 OK\n')
    cl.send('Content-Type: text/html\n')
    print()
    cl.sendall(html)
    cl.close()
    print("Connection closed and waiting for next connection")

# Close socket if CTRL-C is press
except KeyboardInterrupt:
  s.close()