#        _          _          _ _
#  _ __ (_)_  _____| | ___  __| (_)
# | '_ \| \ \/ / _ \ |/ _ \/ _` | |
# | |_) | |>  <  __/ |  __/ (_| | |
# | .__/|_/_/\_\___|_|\___|\__,_|_|
# |_|
# https://links.pixeledi.eu
# Pico 2 W - Webserver Motor Control

import socket
from time import sleep

import network
from machine import Pin

# Motor
in1 = Pin(19, Pin.OUT)
in2 = Pin(18, Pin.OUT)


def motor_stop():
    in1.off()
    in2.off()


# WLAN verbinden
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("bytebunker", "binarybuffer")

print("Verbinde mit WLAN...")
while not wlan.isconnected():
    sleep(1)

ip = wlan.ifconfig()[0]
print(f"Webserver läuft auf: http://{ip}")

# Socket erstellen
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

html = """HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial;
            text-align: center;
            padding: 50px;
            background: #2c3e50;
            color: white;
        }
        button {
            font-size: 30px;
            padding: 30px 60px;
            margin: 20px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
        }
        .aus { background: #e74c3c; color: white; }
        .ein { background: #3498db; color: white; }
    </style>
</head>
<body>
    <h1>pixeledi Motor Steuerung</h1>
    <a href="/ausfahren"><button class="aus">AUSFAHREN</button></a><br>
    <a href="/einfahren"><button class="ein">EINFAHREN</button></a>
</body>
</html>
"""

while True:
    try:
        cl, addr = s.accept()
        request = cl.recv(1024).decode()

        if "/ausfahren" in request:
            print("AUSFAHREN")
            in2.on()
            in1.off()
            sleep(2)
            motor_stop()

        elif "/einfahren" in request:
            print("EINFAHREN")
            in1.on()
            in2.off()
            sleep(2)
            motor_stop()

        cl.send(html)
        cl.close()

    except:
        pass
