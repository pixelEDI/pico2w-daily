#        _          _          _ _
#  _ __ (_)_  _____| | ___  __| (_)
# | '_ \| \ \/ / _ \ |/ _ \/ _` | |
# | |_) | |>  <  __/ |  __/ (_| | |
# | .__/|_/_/\_\___|_|\___|\__,_|_|
# |_|
# https://links.pixeledi.eu
# Pico 2 W - RP2350 | 10.2025

# HW504          →  Pico 2
# ──────────────────────────
# GND            →  GND
# +V             →  3V3 (Pin 36)
# VRx            →  (nicht anschließen)
# VRy            →  GPIO 26 (ADC0)
# SW             →  (nicht anschließen, oder GPIO 21 wenn du willst)


from time import sleep

from machine import ADC, Pin

# Joystick Y-Achse
joy_y = ADC(26)

# L298N Motor Driver
in1 = Pin(19, Pin.OUT)
in2 = Pin(18, Pin.OUT)


def motor_stop():
    in1.off()
    in2.off()


while True:
    value = joy_y.read_u16()

    if value < 25000:
        # Joystick nach oben = ausfahren
        in2.on()
        in1.off()
        print(f">> Ausfahren | {value}")

    elif value > 40000:
        # Joystick nach unten = einfahren
        in1.on()
        in2.off()
        print(f"<< Einfahren | {value}")

    else:
        # Mittelstellung = Stop
        motor_stop()
        # print(f"== Stop | {value}")

    sleep(0.05)
