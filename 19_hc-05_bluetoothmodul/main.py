#        _          _          _ _
#  _ __ (_)_  _____| | ___  __| (_)
# | '_ \| \ \/ / _ \ |/ _ \/ _` | |
# | |_) | |>  <  __/ |  __/ (_| | |
# | .__/|_/_/\_\___|_|\___|\__,_|_|
# |_|
# https://links.pixeledi.eu
# Pico 2 W - RP2350 | 02.2026

from time import sleep

from machine import UART, Pin

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

in1 = Pin(19, Pin.OUT)
in2 = Pin(18, Pin.OUT)

print("Bluetooth bereit...")

while True:
    if uart.any():
        daten = uart.read().decode("utf-8", "ignore").strip()
        print(f"Empfangen: {daten}")

        if "1" in daten:
            print("AUSFAHREN")
            in2.on()
            in1.off()
            sleep(2)
            in1.off()
            in2.off()

        elif "0" in daten:
            print("EINFAHREN")
            in1.on()
            in2.off()
            sleep(2)
            in1.off()
            in2.off()

    sleep(0.1)
