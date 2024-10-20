# LED Circuit with Raspberry Pi Pico WH

This guide demonstrates how to set up a basic circuit using an LED, a resistor, and a Raspberry Pi Pico WH.

## Components Table

| Component           | Description                                         | Pin Connection            | Image                                       |
|---------------------|-----------------------------------------------------|---------------------------|---------------------------------------------|
| Raspberry Pi Pico WH | Microcontroller with built-in WiFi                  | GPIO 15 for LED, GND pin   | <img src="https://path-to-your-image/rp-pico-wh.png" alt="Raspberry Pi Pico WH" width="100">  |
| LED                 | Long leg (anode) connects to Pico, short leg to resistor | Anode to GPIO 15           | <img src="https://path-to-your-image/led.png" alt="LED" width="100">  |
| Resistor            | 220Ω or 330Ω resistor to limit current               | Between LED cathode and GND| <img src="https://github.com/user-attachments/assets/5a9a6009-1f72-456d-8f71-78e0e07ad844" alt="Resistor" width="100">  |
| Breadboard          | For easier wiring and connecting components          | -                         | <img src="https://github.com/user-attachments/assets/69cd2ff4-8c64-456c-b3e9-8d733243dafc" alt="Breadboard" width="150">  |
| Jumper Wires        | Male-to-male wires to connect Pico, LED, resistor    | GPIO pins, GND             | <img src="https://github.com/user-attachments/assets/487d08a0-3748-4128-9afe-afb3e19365f8" alt="Jumper Wires" width="150">  |
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

