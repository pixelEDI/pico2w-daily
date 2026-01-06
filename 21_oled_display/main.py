#        _          _          _ _
#  _ __ (_)_  _____| | ___  __| (_)
# | '_ \| \ \/ / _ \ |/ _ \/ _` | |
# | |_) | |>  <  __/ |  __/ (_| | |
# | .__/|_/_/\_\___|_|\___|\__,_|_|
# |_|
# https://links.pixeledi.eu
# Pico 2 W - RP2350 | 02.2025
# Tag 20: OLED Display - Position und Status anzeigen

# === SSD1306 Library Installation ===
# Methode 1 (einfachste):
#   mpremote mip install ssd1306
#
# Methode 2 (manuell):
#   wget https://raw.githubusercontent.com/micropython/micropython-lib/master/micropython/drivers/display/ssd1306/ssd1306.py
#   mpremote fs cp ssd1306.py :
#
# === Code Upload ===
#   mpremote fs cp main.py :main.py
#   mpremote reset
#
# === Verkabelung ===
# SSD1306 OLED:
#   VCC → 3V3
#   GND → GND
#   SCL → GPIO 5
#   SDA → GPIO 4
# Buttons:
#   Button 1 → GPIO 21 (Einfahren)
#   Button 2 → GPIO 22 (Ausfahren)
# L298N:
#   IN1 → GPIO 19
#   IN2 → GPIO 18

from time import sleep

from machine import I2C, Pin
from ssd1306 import SSD1306_I2C

# OLED Display Setup
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

# Buttons
button1 = Pin(21, Pin.IN, Pin.PULL_DOWN)  # Einfahren
button2 = Pin(22, Pin.IN, Pin.PULL_DOWN)  # Ausfahren

# L298N Motor Driver
in1 = Pin(19, Pin.OUT)
in2 = Pin(18, Pin.OUT)


def motor_stop():
    in1.off()
    in2.off()


def update_display(status, position, distance_cm):
    oled.fill(0)

    # Header
    oled.fill_rect(0, 0, 128, 12, 1)
    oled.text("LINEARANTRIEB", 20, 2, 0)

    # Status mit Icon
    if status == ">>":
        icon = ">"
    elif status == "<<":
        icon = "<"
    else:
        icon = "="

    oled.text(f"{icon} {status:<12}", 0, 18)

    # Position numerisch
    oled.text(f"{distance_cm:.1f}cm / 5.0cm", 0, 32)

    # Fortschrittsbalken
    oled.rect(4, 48, 120, 12, 1)
    bar = int((position / 100) * 116)
    if bar > 0:
        oled.fill_rect(6, 50, bar, 8, 1)

    oled.show()


# START EINGEFAHREN (0%)
position = 0
SPEED = 0.4  # 4mm/s = 0.4cm/s

# Startup Screen
distance = (position / 100) * 5.0
update_display("Eingefahren", position, distance)
sleep(1)

while True:
    distance = (position / 100) * 5.0  # 0-5cm

    if button1.value() == 1:
        # Einfahren
        in1.on()
        in2.off()
        if position > 0:
            position = max(0, position - 0.8)
        update_display("Einfahren", position, distance)

    elif button2.value() == 1:
        # Ausfahren
        in2.on()
        in1.off()
        if position < 100:
            position = min(100, position + 0.8)
        update_display("Ausfahren", position, distance)

    else:
        # Stop
        motor_stop()
        update_display("Stop", position, distance)

    sleep(0.1)
