# LED Circuit with Raspberry Pi Pico WH

This guide demonstrates how to set up a basic circuit using an LED, a resistor, and a Raspberry Pi Pico WH.

## Components Table

| Component           | Description                                         | Pin Connection            |
|---------------------|-----------------------------------------------------|---------------------------|
| <img src="https://path-to-your-image/rp-pico-wh.png" alt="Raspberry Pi Pico WH" width="100">  | Microcontroller with built-in WiFi                  | GPIO 15 for LED, GND pin   |
| <img src="https://path-to-your-image/led.png" alt="LED" width="100">  | Long leg (anode) connects to Pico, short leg to resistor | Anode to GPIO 15           |
| <img src="https://path-to-your-image/resistor.png" alt="Resistor" width="100">  | 220Ω or 330Ω resistor to limit current               | Between LED cathode and GND|
| <img src="https://path-to-your-image/breadboard.png" alt="Breadboard" width="100">  | For easier wiring and connecting components          | -                         |
| <img src="https://path-to-your-image/jumper-wires.png" alt="Jumper Wires" width="100">  | Male-to-male wires to connect Pico, LED, resistor    | GPIO pins, GND             |
| <img src="https://path-to-your-image/usb-cable.png" alt="USB Cable" width="100">  | For powering the Raspberry Pi Pico WH                | Micro-USB port             |

## Circuit Diagram

<div align="center">
  <img src="https://github.com/user-attachments/assets/63f12fa1-1400-4b81-b04c-596395311abe" alt="README" width="300px" height="300px">
</div>

## Connections Breakdown

| **Pin**      | **Component**  | **Connection**       |
|--------------|----------------|----------------------|
| GPIO 15      | LED (Anode)    | Long leg of LED      |
| GND          | Resistor       | Connect resistor end |
| Resistor end | LED (Cathode)  | Short leg of LED     |

