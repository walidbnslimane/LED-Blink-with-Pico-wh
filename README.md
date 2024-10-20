# LED Blink Project with Raspberry Pi Pico WH

## Project Overview
This project demonstrates how to blink an external and internal LED on the Raspberry Pi Pico WH simultaneously. After 1 second, both LEDs turn off at the same time. This simple project is ideal for beginners to learn about basic GPIO control and programming with the Raspberry Pi Pico.

## Components Required
- Raspberry Pi Pico WH
- External LED (e.g., 5mm LED)
- Resistor (220Ω for external LED)
- Breadboard and jumper wires (for external LED connections)

## Circuit Diagram
![Circuit Diagram](https://github.com/user-attachments/assets/63f12fa1-1400-4b81-b04c-596395311abe)  

### Connections
- **Internal LED**: 
  - Connect the internal LED to GPIO0 pin "LED"
- **External LED**:
  - Connect the longer leg (anode) of the external LED to resistor.
  - connect resistor to pin 15 (GP15)
  - Connect the shorter leg (cathode) to the ground (GND).

## Code Explanation
```python
from machine import Pin
import time

# Setup for internal and external LEDs
internal_led = Pin("LED", Pin.OUT)  # Internal LED
external_led = Pin(15, Pin.OUT)    # External LED (GP15)

while True:
    # Turn on both LEDs
    internal_led.on()
    external_led.on()
    time.sleep(1)  # Keep LEDs on for 1 second

    # Turn off both LEDs
    internal_led.off()
    external_led.off()
    time.sleep(1)  # Wait for 1 second before next iteration
