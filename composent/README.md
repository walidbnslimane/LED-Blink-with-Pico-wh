# LED Circuit with Raspberry Pi Pico WH

This guide demonstrates how to set up a basic circuit using an LED, a resistor, and a Raspberry Pi Pico WH.

## Components Table

| Component           | Description                                         | Pin Connection            |
|---------------------|-----------------------------------------------------|---------------------------|
| **Raspberry Pi Pico WH** | Microcontroller with built-in WiFi                  | GPIO 15 for LED, GND pin   |
| **LED**             | Long leg (anode) connects to Pico, short leg to resistor | Anode to GPIO 15           |
| **Resistor**        | 220Ω or 330Ω resistor to limit current               | Between LED cathode and GND|
| **Breadboard**      | For easier wiring and connecting components          | -                         |
| **Jumper Wires**    | Male-to-male wires to connect Pico, LED, resistor    | GPIO pins, GND             |
| **USB Cable**       | For powering the Raspberry Pi Pico WH                | Micro-USB port             |

## Connections Breakdown

| **Pin**      | **Component**  | **Connection**       |
|--------------|----------------|----------------------|
| GPIO 15      | LED (Anode)    | Long leg of LED      |
| GND          | Resistor       | Connect resistor end |
| Resistor end | LED (Cathode)  | Short leg of LED     |

