#        _          _          _ _
#  _ __ (_)_  _____| | ___  __| (_)
# | '_ \| \ \/ / _ \ |/ _ \/ _` | |
# | |_) | |>  <  __/ |  __/ (_| | |
# | .__/|_/_/\_\___|_|\___|\__,_|_|
# |_|
# https://links.pixeledi.eu
# Pico 2 W - RP2350 | 02.2026

from time import sleep, ticks_diff, ticks_ms

import neopixel
from machine import Pin

# Buttons
button1 = Pin(21, Pin.IN, Pin.PULL_DOWN)  # Einfahren
button2 = Pin(22, Pin.IN, Pin.PULL_DOWN)  # Ausfahren

# L298N Motor Driver
in1 = Pin(19, Pin.OUT)
in2 = Pin(18, Pin.OUT)

# NeoPixel Ring - 12 LEDs
ring = neopixel.NeoPixel(Pin(26), 12)


def motor_stop():
    in1.off()
    in2.off()


def alle_aus():
    for i in range(12):
        ring[i] = (0, 0, 0)
    ring.write()


def led_rot():
    for i in range(12):
        ring[i] = (30, 0, 0)
    ring.write()


def led_blau():
    for i in range(12):
        ring[i] = (0, 0, 30)
    ring.write()


# Lauflicht Variablen
led_index = 0
letzter_wechsel = ticks_ms()

while True:
    # Grüner Lauflicht-Effekt
    if ticks_diff(ticks_ms(), letzter_wechsel) >= 100:
        ring[led_index] = (0, 30, 0)
        ring.write()
        led_index += 1

        if led_index >= 12:
            led_index = 0
            alle_aus()

        letzter_wechsel = ticks_ms()

    # Button Check
    if button1.value() == 1:
        led_blau()
        in1.on()
        in2.off()
        sleep(0.5)
        motor_stop()
        alle_aus()
        led_index = 0
        letzter_wechsel = ticks_ms()
        sleep(0.3)

    elif button2.value() == 1:
        led_rot()
        in2.on()
        in1.off()
        sleep(0.5)
        motor_stop()
        alle_aus()
        led_index = 0
        letzter_wechsel = ticks_ms()
        sleep(0.3)

    sleep(0.01)
