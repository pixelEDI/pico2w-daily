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

# Buttons
button1 = Pin(21, Pin.IN, Pin.PULL_DOWN)  # Einfahren
button2 = Pin(22, Pin.IN, Pin.PULL_DOWN)  # Ausfahren

# L298N Motor Driver
in1 = Pin(19, Pin.OUT)
in2 = Pin(18, Pin.OUT)


def motor_stop():
    in1.off()
    in2.off()


while True:
    if button1.value() == 1:
        in1.on()
        in2.off()
        sleep(1.5)
        motor_stop()
        sleep(0.3)

    elif button2.value() == 1:
        in2.on()
        in1.off()
        sleep(1.5)
        motor_stop()
        sleep(0.3)

    sleep(0.1)
