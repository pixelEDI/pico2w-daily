#        _          _          _ _
#  _ __ (_)_  _____| | ___  __| (_)
# | '_ \| \ \/ / _ \ |/ _ \/ _` | |
# | |_) | |>  <  __/ |  __/ (_| | |
# | .__/|_/_/\_\___|_|\___|\__,_|_|
# |_|
# https://links.pixeledi.eu
# Pico 2 W - RP2350 | 02.2026

# Pin A (unten links)  → 3.3V
# Pin 1 (oben ganz links)         → GPIO
# Pin 2 (oben links daneben)   → GND

from time import sleep

from machine import ADC, Pin

poti = ADC(28)
in1 = Pin(19, Pin.OUT)
in2 = Pin(18, Pin.OUT)


def motor_stop():
    in1.off()
    in2.off()


while True:
    value = poti.read_u16()

    if value < 30000:
        # Poti links = Einfahren
        in2.on()
        in1.off()
        print(f" >> Ausfahren | {value}")

    elif value > 50000:
        # Poti rechts = Ausfahren
        in1.on()
        in2.off()
        print(f" << Einfahren | {value}")

    else:
        # Mitte = Stop
        motor_stop()
        # print(f"== Stop | {value}")

    sleep(0.05)
