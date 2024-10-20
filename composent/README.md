# LED Circuit with Raspberry Pi Pico WH

This guide demonstrates how to set up a basic circuit using an LED, a resistor, and a Raspberry Pi Pico WH.

## Components Table

| Component           | Description                                         | Pin Connection            |
|---------------------|-----------------------------------------------------|---------------------------|
| **Raspberry Pi Pico WH** <br> <img src="https://path-to-your-image/rp-pico-wh.png" alt="Raspberry Pi Pico WH" width="100">  | Microcontroller with built-in WiFi                  | GPIO 15 for LED, GND pin   |
| **LED** <br> <img src="https://path-to-your-image/led.png" alt="LED" width="100">  | Long leg (anode) connects to Pico, short leg to resistor | Anode to GPIO 15           |

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

