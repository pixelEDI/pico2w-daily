#        _          _          _ _
#  _ __ (_)_  _____| | ___  __| (_)
# | '_ \| \ \/ / _ \ |/ _ \/ _` | |
# | |_) | |>  <  __/ |  __/ (_| | |
# | .__/|_/_/\_\___|_|\___|\__,_|_|
# |_|
# https://links.pixeledi.eu
# Pico 2 W - RP2350 | 02.2026


# === BH1750 Library ===
#   wget https://github.com/flrrth/pico-bh1750/raw/main/bh1750/bh1750.py
#   mpremote connect /dev/ttyACM1 fs cp *.py :
# === Verkabelung ===
# BH1750 Lichtsensor:
#   VCC → 3V3
#   GND → GND
#   SCL → GPIO 5 (shared mit OLED)
#   SDA → GPIO 4 (shared mit OLED)
# L298N:
#   IN1 → GPIO 19
#   IN2 → GPIO 18

from time import sleep

from bh1750 import BH1750
from machine import I2C, Pin

# I2C Setup
i2c0_sda = Pin(4)
i2c0_scl = Pin(5)
i2c0 = I2C(0, sda=i2c0_sda, scl=i2c0_scl)

# BH1750 Sensor
bh1750 = BH1750(0x23, i2c0)

# L298N Motor Driver
in1 = Pin(19, Pin.OUT)
in2 = Pin(18, Pin.OUT)


def motor_stop():
    in1.off()
    in2.off()


# Schwellwert (in Lux) - anpassen nach Bedarf!
THRESHOLD = 200

print("BH1750 Linear-Steuerung")
print(f"Schwellwert: {THRESHOLD} Lux")
print("Hell (>{THRESHOLD}) = Ausfahren")
print("Dunkel (<{THRESHOLD}) = Einfahren")

while True:
    lux = bh1750.measurement

    if lux > THRESHOLD:
        # Hell = Ausfahren
        in2.on()
        in1.off()
        print(f">> Ausfahren | {lux:.1f} Lux")

    else:
        # Dunkel = Einfahren
        in1.on()
        in2.off()
        print(f"<< Einfahren | {lux:.1f} Lux")

    sleep(0.5)
