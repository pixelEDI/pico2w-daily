# 🚀 29 Tage Raspberry Pi Pico 2W Challenge
**DC Motor-Steuerung Februar 2026** | Ein Motor viele Steuerungsmethoden!

## 🎓 Online-Kurs zur Challenge
Lerne alles Schritt für Schritt im **Pico 2W Komplettkurs**: https://pixeledi.eu/akademie/pico  
💰 **Rabattcode sichern:** https://pixeledi.eu/daily

## 🔌 Basis-Verkabelung
| Pico 2W | → | L298N | → | Extern |
|---------|---|-------|---|--------|
| Pin 19 (GPIO14) | → | IN1 | | |
| Pin 18 (GPIO13) | → | IN2 | | |
| GND | → | GND | ← | Netzteil (-) |
| | | +12V | ← | Netzteil (+) |
| | | OUT1/OUT2 | → | Linearantrieb |

**PWM-Steuerung (optional):**

## 🛒 Materialliste

**🔧 Basis-Komponenten**
- 🔌 Pico 2W: https://amzn.to/4jpBUMp
- ⚡ Linearantrieb 12V: https://amazon.de/dp/B09JZHPG7P
- 🎛️ L298N Motor Driver: https://amzn.to/4ps25Ud
- 🔋 Labornetzteil: https://amzn.to/4jqE1Qd
- 🔘 Bunte Buttons: https://amzn.to/48MdPZm
- 🔲 Mini Breadboard: https://amzn.to/3X5BLnv
- 🌈 Litzen Set: https://amzn.to/43ilJbU
- 💡 LED Sortiment: https://amzn.to/426MhfP
- 🚦 LED Ampel: https://amzn.to/47uY7UU
- 🔄 USB-C Adapter: https://amzn.to/4qbcl4R

**📟 Sensoren & Module**
- 🎚️ 10kΩ Poti: https://amzn.to/4aEKbd7
- 🕹️ Joystick: https://amzn.to/4shJeOa
- 🧲 Hall-Sensor A3144: https://amzn.to/4bpGwA2
- 💡 BH1750 Licht: https://amzn.to/4aJDc2H
- 🔄 Rotary Encoder: https://amzn.to/3Yp0u6t
- 👆 Touch TTP223: https://amzn.to/3Yp0u6t
- 🌀 SW-420 Vibration: https://amzn.to/4397cjJ
- 📡 Meshtastic SX1262: https://amzn.to/49E7Zg6

**🔧 Expansion Boards**
- Gravity Board: https://dfrobot.com/product-2393.html | [Wiki](https://wiki.dfrobot.com/PICO_Gravity_Expansion_Shield_SKU_DFR0848) | [3D Case](https://printables.com/model/1438611)
- IO Board: https://dfrobot.com/product-2390.html | [Wiki](https://wiki.dfrobot.com/PICO_IO_Expansion_Shield_SKU_DFR0836) | [3D Case](https://printables.com/model/1438612)
- SW-420 Magnetic Mount: https://printables.com/model/228197

**Hinweis:** Die Amazon-Links sind Affiliate-Links – du zahlst den gleichen Preis, ich erhalte eine kleine Provision zur Unterstützung des Projekts.

## 📤 Upload auf Pico
```bash
mpremote fs cp tagXX_*/main.py :main.py  # Hochladen
mpremote reset                            # Neustart
mpremote run tagXX_*/main.py             # Direkt ausführen
```

🎥 **YouTube:** https://youtube.com/@pixeledi
