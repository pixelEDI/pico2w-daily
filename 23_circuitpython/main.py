#        _          _          _ _
#  _ __ (_)_  _____| | ___  __| (_)
# | '_ \| \ \/ / _ \ |/ _ \/ _` | |
# | |_) | |>  <  __/ |  __/ (_| | |
# | .__/|_/_/\_\___|_|\___|\__,_|_|
# |_|
# https://links.pixeledi.eu
# Pico 2 W - RP2350 | 02.2026
# https://circuitpython.org/
import time

import board
import digitalio

# Buttons
button1 = digitalio.DigitalInOut(board.GP21)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.DOWN

button2 = digitalio.DigitalInOut(board.GP22)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.DOWN

# L298N Motor Driver
in1 = digitalio.DigitalInOut(board.GP19)
in1.direction = digitalio.Direction.OUTPUT

in2 = digitalio.DigitalInOut(board.GP18)
in2.direction = digitalio.Direction.OUTPUT


def motor_stop():
    in1.value = False
    in2.value = False


while True:
    if button1.value:
        in1.value = True
        in2.value = False
        time.sleep(0.5)
        motor_stop()
        time.sleep(0.3)
    elif button2.value:
        in2.value = True
        in1.value = False
        time.sleep(0.5)
        motor_stop()
        time.sleep(0.3)
    time.sleep(0.1)
