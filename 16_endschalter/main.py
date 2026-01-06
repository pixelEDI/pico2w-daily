#        _          _          _ _
#  _ __ (_)_  _____| | ___  __| (_)
# | '_ \| \ \/ / _ \ |/ _ \/ _` | |
# | |_) | |>  <  __/ |  __/ (_| | |
# | .__/|_/_/\_\___|_|\___|\__,_|_|
# |_|
# https://links.pixeledi.eu
# Pico 2 W - RP2350 | 02.2026


from time import sleep

from machine import Pin

# Button
button = Pin(21, Pin.IN, Pin.PULL_DOWN)

# Endschalter: Pin2→GPIO12, Pin1→GND
endschalter = Pin(12, Pin.IN, Pin.PULL_UP)

# L298N Motor Driver
in1 = Pin(19, Pin.OUT)
in2 = Pin(18, Pin.OUT)


def motor_stop():
    in1.off()
    in2.off()


ausgefahren = False

while True:
    if button.value() == 1:

        if not ausgefahren:
            # Ausfahren bis Endschalter gedrückt
            print("AUSFAHREN...")
            in2.on()
            in1.off()

            while endschalter.value() == 1:  # HIGH = nicht gedrückt
                sleep(0.01)

            motor_stop()
            print("Endschalter erreicht!")
            ausgefahren = True

        else:
            # Einfahren
            print("EINFAHREN...")
            in1.on()
            in2.off()
            sleep(2)
            motor_stop()
            ausgefahren = False

        while button.value() == 1:
            sleep(0.01)

        sleep(0.3)

    sleep(0.1)
