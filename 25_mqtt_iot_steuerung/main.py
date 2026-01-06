#        _          _          _ _
#  _ __ (_)_  _____| | ___  __| (_)
# | '_ \| \ \/ / _ \ |/ _ \/ _` | |
# | |_) | |>  <  __/ |  __/ (_| | |
# | .__/|_/_/\_\___|_|\___|\__,_|_|
# |_|
# https://links.pixeledi.eu
# Pico 2 W - RP2350 | 02.2026

# https://github.com/micropython/micropython-lib/blob/master/micropython/umqtt.simple/example_sub_led.py

from time import sleep

import network
from machine import Pin
from umqtt import MQTTClient

# MQTT Einstellungen
MQTT_SERVER = "65.21.105.35"
MQTT_USER = "pixeledi_pico"
MQTT_PASS = "Mqttpico1"

# WiFi Einstellungen
ssid = "bytebunker"
password = "binarybuffer"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# L298N Motor Driver
in1 = Pin(19, Pin.OUT)
in2 = Pin(18, Pin.OUT)


def motor_stop():
    in1.value(0)
    in2.value(0)


def motor_einfahren():
    print("← Einfahren")
    in2.value(1)
    in1.value(0)


def motor_ausfahren():
    print("→ Ausfahren")
    in1.value(1)
    in2.value(0)


motor_stop()


def connect_wifi():
    connection_timeout = 10
    while connection_timeout > 0:
        if wlan.status() >= 3:
            break
        connection_timeout -= 1
        print("Waiting for Wi-Fi...")
        sleep(1)

    if wlan.status() != 3:
        raise RuntimeError("Failed to establish a network connection")
    else:
        print("Connection successful!")
        network_info = wlan.ifconfig()
        print("IP address:", network_info[0])


def sub_cb(topic, msg):
    print((topic, msg))

    if topic == b"linearantrieb/einfahren":
        if msg == b"1":
            motor_einfahren()
        elif msg == b"0":
            motor_stop()

    elif topic == b"linearantrieb/ausfahren":
        if msg == b"1":
            motor_ausfahren()
        elif msg == b"0":
            motor_stop()


def main():
    connect_wifi()
    c = MQTTClient(
        "pico_linearantrieb", MQTT_SERVER, user=MQTT_USER, password=MQTT_PASS
    )
    c.set_callback(sub_cb)
    c.connect()

    # Subscribe auf beide Topics
    c.subscribe(b"linearantrieb/einfahren")
    c.subscribe(b"linearantrieb/ausfahren")

    print("MQTT connected - waiting for messages...")

    while True:
        c.wait_msg()


main()
