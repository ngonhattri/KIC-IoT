import network
import socket
import sys
import time

# Default port number for WWW
PORT = 80
switch_state = "OFF"
# Make HTTP header and HTML contents
def web_page():
  html = """<html><head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
     integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <style>
        html {
            font-family: Arial;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }

        .button {
            background-color: #ce1b0e;
            border: none;
            color: white;
            padding: 16px 40px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }

        .button1 {
            background-color: #000000;
        }
    </style>
</head>

<body>
    <h2>ESP MicroPython Web Server</h2>
    <p>SWITCH state: <strong>""" + switch_state + """</strong></p>
    <p>
        <i class="fas fa-lightbulb fa-3x" style="color:#c81919;"></i>
        <a href=\"?switch_on\"><button class="button">SWITCH ON</button></a>
    </p>
    <p>
        <i class="far fa-lightbulb fa-3x" style="color:#000000;"></i>
        <a href=\"?switch_off\"><button class="button button1">SWITCH OFF</button></a>
    </p>
</body>

</html>"""
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

    response = web_page()
    cl.send('HTTP/1.1 200 OK\n')
    cl.send('Content-Type: text/html\n')
    cl.sendall(response)
    cl.close()
    print("Connection closed and waiting for next connection")

# Close socket if CTRL-C is press
except KeyboardInterrupt:
  s.close()