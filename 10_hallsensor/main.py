#        _          _          _ _
#  _ __ (_)_  _____| | ___  __| (_)
# | '_ \| \ \/ / _ \ |/ _ \/ _` | |
# | |_) | |>  <  __/ |  __/ (_| | |
# | .__/|_/_/\_\___|_|\___|\__,_|_|
# |_|
# https://links.pixeledi.eu
# Pico 2 W - RP2350 | 10.2025

# === VERKABELUNG A3144 Hall-Sensor ===
# Links:  Signal → GPIO 16 (mit 10k Pull-up zu VCC)
# Mitte:  GND    → GND
# Rechts: VCC    → 3.3V (mit 10k zu Signal)
#
# Schema: [Signal] [GND] [VCC]
#            |       |      |
#         GPIO16   GND   3.3V
#         (10k Widerstand zwischen VCC und Signal)

from time import sleep

from machine import Pin

# Hall-Sensor A3144
hall = Pin(16, Pin.IN, Pin.PULL_UP)  # A3144 ist aktiv LOW

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


print("Hall-Sensor aktiv - halte Magnet ran...")

while True:
    # Debug: Wert ausgeben
    wert = hall.value()
    print(f"Hall-Sensor Wert: {wert}")

    if wert == 0:  # Magnet erkannt (aktiv LOW)
        print(">>> MAGNET ERKANNT! <<<")
        motor_ausfahren(2)  # 2 Sekunden ausfahren
        sleep(0.5)  # Kurz warten
        motor_einfahren(2)  # 2 Sekunden einfahren
        sleep(1)  # Pause

    sleep(0.5)
