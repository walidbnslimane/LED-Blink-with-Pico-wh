# LED Circuit with Raspberry Pi Pico WH

This guide demonstrates how to set up a basic circuit using an LED, a resistor, and a Raspberry Pi Pico WH.

## Components Table

| Component           | Description                                         | Pin Connection            | Image                                       |
|---------------------|-----------------------------------------------------|---------------------------|---------------------------------------------|
| Raspberry Pi Pico WH | Microcontroller with built-in WiFi                  | GPIO 15 for LED, GND pin   | <img src="https://github.com/user-attachments/assets/3d182aa3-03d6-452b-a237-287b00e4ef78" width="270" >  |
| LED                 | Long leg (anode) connects to Pico, short leg to resistor | Anode to GPIO 15           | <img src="https://github.com/user-attachments/assets/265a4442-a139-4051-82f5-eb93e849d90a" alt="LED" width="270">  |
| Resistor            | 220Ω or 330Ω resistor to limit current               | Between LED cathode and GND| <img src="https://github.com/user-attachments/assets/ce9a677e-3ba4-4b60-9420-2f1fa8915891" alt="Resistor" width="270">  |
| Breadboard          | For easier wiring and connecting components          | -                         | <img src="https://github.com/user-attachments/assets/0b694d76-3eea-4123-a352-6cec240d29b1" alt="Breadboard" width="270">  |
| Jumper Wires        | Male-to-male wires to connect Pico, LED, resistor    | GPIO pins, GND             | <img src="https://github.com/user-attachments/assets/b21f7fa1-e0f0-46e0-b93c-fa01bac3a849" alt="Jumper Wires" width="270">  |
## Circuit Diagram



## Connections Breakdown

| **Pin**      | **Component**  | **Connection**       |
|--------------|----------------|----------------------|
| GPIO 15      | LED (Anode)    | Long leg of LED      |
| GND          | Resistor       | Connect resistor end |
| Resistor end | LED (Cathode)  | Short leg of LED     |

