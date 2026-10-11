What is an embedded System?
- Embedded systems are computer systems designed for a specific function.
- The opposite is a gnereal purpose computer where it can perform calls, games etc
- Examples of an embedded system is vending machines atms etc

### What is an embeded System?
"An embedded system is a computer system with a single dedicated function. This function is prevelant in its hardware"
- **microprocessor**: CPU on a single integrated circuit. It has to interface with mem and peripherals **off** the chip
- **microcontroller:** Cpu **with** memory, i/o ports, timers & other peripherals all on the same chip

A vending Machine has 

| Example     | **Inputs** | **Outputs** | **Control**     | Function                     |
| ----------- | ---------- | ----------- | --------------- | ---------------------------- |
| Vending Mac | Keypad     | LCD Display | Microcontrolelr | Read input -> present output |
|             |            |             |                 |                              |


# Lecture 2

### Why is a microprocessor inconvenient for embedded sustem use?
1. They dont have enough memory
2. They use too much power

### What is AVR?
**Automatic Voltage Regulator**
- Maintains constant safe voltage level for electrical equipment


### Data I / O
- The Atmega32U2 has 23 PIO pins, split over three 8-bit ports: Port B, Port C, and Port D. PC3 is unused.
- Each pin can be configured as an input
- The I / O Port registers control the flow of in / out to / from the microcontroller
- Each I / o Port has three 8 bit registers which control its operation
- For a generic Port x, there registers regis are 
	- DDRx: The Data Direction Register for Port X
	- PORTx: The output data register for Port x
	- PINx: The Port INput register for Port x
- Across the three registers a specific bit controls a specific pin for example pin PC2 is controlled by the bit 2 in each for DDRC, PORTC and PINC

**DDR or Data Direction**


eac pin controls the direction of data flows
- if data is coming in from a button the pin is an inout
- if data is being sent out  LED then the pin is an output
- A DDRx bit value of zero means the pin is an input
- A bit value of one means the pin is an output
- DDR usually only need to be configured once at startup 
- 0 = input 0 = output

**PINx**:

