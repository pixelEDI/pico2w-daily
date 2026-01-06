#        _          _          _ _
#  _ __ (_)_  _____| | ___  __| (_)
# | '_ \| \ \/ / _ \ |/ _ \/ _` | |
# | |_) | |>  <  __/ |  __/ (_| | |
# | .__/|_/_/\_\___|_|\___|\__,_|_|
# |_|
# https://links.pixeledi.eu
# Pico 2 W - RP2350 | 02.2026


from time import sleep, ticks_diff, ticks_ms

from machine import Pin

# Buttons
button1 = Pin(21, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(22, Pin.IN, Pin.PULL_DOWN)

# Motor Driver
in1 = Pin(19, Pin.OUT)
in2 = Pin(18, Pin.OUT)

# Debounce
letzter_druck = 0
DEBOUNCE_MS = 300


def motor_stop():
    in1.off()
    in2.off()


def button1_handler(pin):
    global letzter_druck

    # Debounce
    if ticks_diff(ticks_ms(), letzter_druck) < DEBOUNCE_MS:
        return

    letzter_druck = ticks_ms()

    print("Button 1 - EINFAHREN")
    in1.on()
    in2.off()
    sleep(0.5)
    motor_stop()


def button2_handler(pin):
    global letzter_druck

    # Debounce
    if ticks_diff(ticks_ms(), letzter_druck) < DEBOUNCE_MS:
        return

    letzter_druck = ticks_ms()

    print("Button 2 - AUSFAHREN")
    in2.on()
    in1.off()
    sleep(0.5)
    motor_stop()


# Interrupts registrieren
button1.irq(trigger=Pin.IRQ_RISING, handler=button1_handler)
button2.irq(trigger=Pin.IRQ_RISING, handler=button2_handler)

print("Bereit - CPU ist frei!")

# Hauptschleife macht was anderes
counter = 0
while True:
    counter += 1
    if counter % 50 == 0:
        print(f"CPU zählt weiter: {counter}")
    sleep(0.1)
