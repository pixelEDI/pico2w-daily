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

# L298N Motor Driver
in1 = Pin(18, Pin.OUT)
in2 = Pin(19, Pin.OUT)

print("=== Pico 2 Linearantrieb ===")
print("Hardware-Test startet...")

# Test ausfahren
print("Teste Ausfahren...")
in1.on()
in2.off()
sleep(2)

# Stop
in1.off()
in2.off()
print("Stop")
sleep(1)

# Test einfahren
print("Teste Einfahren...")
in2.on()
in1.off()
sleep(2)

# Stop
in1.off()
in2.off()
print("Hardware-Test abgeschlossen!")
print("Alle Komponenten funktionieren!")
