#        _          _          _ _
#  _ __ (_)_  _____| | ___  __| (_)
# | '_ \| \ \/ / _ \ |/ _ \/ _` | |
# | |_) | |>  <  __/ |  __/ (_| | |
# | .__/|_/_/\_\___|_|\___|\__,_|_|
# |_|
# https://links.pixeledi.eu
# Pico 2 W - RP2350 | 10.2025
from time import sleep

from machine import Pin

# Vibrationssensor
vibration = Pin(16, Pin.IN, Pin.PULL_DOWN)

# L298N Motor Driver
in1 = Pin(19, Pin.OUT)
in2 = Pin(18, Pin.OUT)


def motor_stop():
    in1.off()
    in2.off()


def motor_ausfahren(dauer):
    in1.on()
    in2.off()
    sleep(dauer)
    motor_stop()


def motor_einfahren(dauer):
    in2.on()
    in1.off()
    sleep(dauer)
    motor_stop()


print("Vibrationssensor aktiv - warte auf Erschuetterung...")

while True:
    if vibration.value() == 1:
        print("Vibration erkannt!")
        motor_ausfahren(2)  # 2 Sekunden ausfahren
        sleep(0.5)  # Kurz warten
        motor_einfahren(2)  # 2 Sekunden einfahren
        sleep(1)  # Pause damit nicht sofort wieder triggert

    sleep(0.1)
