#        _          _          _ _
#  _ __ (_)_  _____| | ___  __| (_)
# | '_ \| \ \/ / _ \ |/ _ \/ _` | |
# | |_) | |>  <  __/ |  __/ (_| | |
# | .__/|_/_/\_\___|_|\___|\__,_|_|
# |_|
# https://links.pixeledi.eu
# Pico 2 W - RP2350 | 02.2026
# ntptime test

from time import localtime, sleep

import network
import ntptime

# WLAN verbinden
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("bytebunker", "binarybuffer")

print("Verbinde mit WLAN...")
while not wlan.isconnected():
    sleep(1)
print("WLAN verbunden!")

# Zeit vom NTP-Server holen
try:
    ntptime.settime()
    ZEITZONE = 1 * 3600
    print("Zeit aktualisiert!")
except:
    print("NTP-Fehler!")

# Zeit anzeigen
while True:
    t = localtime()
    # Zeitzone addieren
    stunde = (t[3] + 1) % 24  # +1 für MEZ

    print(f"{stunde:02d}:{t[4]:02d}:{t[5]:02d}")
    sleep(1)
