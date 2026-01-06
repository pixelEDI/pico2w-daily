#        _          _          _ _
#  _ __ (_)_  _____| | ___  __| (_)
# | '_ \| \ \/ / _ \ |/ _ \/ _` | |
# | |_) | |>  <  __/ |  __/ (_| | |
# | .__/|_/_/\_\___|_|\___|\__,_|_|
# |_|
# https://links.pixeledi.eu
# Pico 2 W - RP2350 | 02.2026

# WICHTIG: ENA Jumper am L298N muss RAUS sein!
# ENA Pin → GPIO 28
# Poti → GPIO 27 (ADC1)

from time import sleep

from machine import ADC, PWM, Pin

# Buttons
button1 = Pin(21, Pin.IN, Pin.PULL_DOWN)  # Einfahren
button2 = Pin(22, Pin.IN, Pin.PULL_DOWN)  # Ausfahren

# Potentiometer für Geschwindigkeit
poti = ADC(27)

# L298N Motor Driver
in1 = Pin(19, Pin.OUT)
in2 = Pin(18, Pin.OUT)

# PWM für Geschwindigkeit
ena = PWM(Pin(28))
ena.freq(1000)


def motor_stop():
    ena.duty_u16(0)  # PWM aus
    in1.off()
    in2.off()


while True:
    # Geschwindigkeit vom Poti lesen (0-65535)
    speed = poti.read_u16()

    if button1.value() == 1:
        # Einfahren solange Button gedrückt
        ena.duty_u16(speed)
        in1.on()
        in2.off()
    elif button2.value() == 1:
        # Ausfahren solange Button gedrückt
        ena.duty_u16(speed)
        in2.on()
        in1.off()
    else:
        # Kein Button = Motor stop
        motor_stop()
