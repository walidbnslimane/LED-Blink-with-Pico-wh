# LED Circuit with Raspberry Pi Pico WH

This guide demonstrates how to set up a basic circuit using an LED, a resistor, and a Raspberry Pi Pico WH.

## Components Table

| Component           | Description                                         | Pin Connection            | Image                                       |
|---------------------|-----------------------------------------------------|---------------------------|---------------------------------------------|
| Raspberry Pi Pico WH | Microcontroller with built-in WiFi                  | GPIO 15 for LED, GND pin   | <img src="https://github.com/user-attachments/assets/3d182aa3-03d6-452b-a237-287b00e4ef78" width="150" height="145">  |
| LED                 | Long leg (anode) connects to Pico, short leg to resistor | Anode to GPIO 15           | <img src="https://github.com/user-attachments/assets/b92353ea-fafa-42f3-88cc-332ef708080a" alt="LED" width="150">  |
| Resistor            | 220Ω or 330Ω resistor to limit current               | Between LED cathode and GND| <img src="https://github.com/user-attachments/assets/5a9a6009-1f72-456d-8f71-78e0e07ad844" alt="Resistor" width="150">  |
| Breadboard          | For easier wiring and connecting components          | -                         | <img src="https://github.com/user-attachments/assets/69cd2ff4-8c64-456c-b3e9-8d733243dafc" alt="Breadboard" width="150">  |
| Jumper Wires        | Male-to-male wires to connect Pico, LED, resistor    | GPIO pins, GND             | <img src="https://github.com/user-attachments/assets/b7bfddc2-2750-4428-bab8-db537fb9933c" alt="Jumper Wires" width="150">  |
## Circuit Diagram



## Connections Breakdown

| **Pin**      | **Component**  | **Connection**       |
|--------------|----------------|----------------------|
| GPIO 15      | LED (Anode)    | Long leg of LED      |
| GND          | Resistor       | Connect resistor end |
| Resistor end | LED (Cathode)  | Short leg of LED     |

