1. Number Systems & Bit weights
- In a 8 bit controller you are constantly converting between binary hexadecimal and decimal
=
### Bitwise Operators in C


**&** Outputs 1 only if both bits are 1
- **Use:** Clearing / Checking
- 0b1011 & 0b0010 = 0b0010

**|** Outputs if either
- Use: **Setting**
- 0b1000 | 0b0010 = 0b1010

**^** Outputs if different
- Use: **Flipping Single**
- 0b1010 ^ 0b0010 = 0b1000

**~**  Flips all
- ~0x12 (0b00010000) = 16 = 0x10

### Functions
**Set a bit (turn it to 1):**
REG |= (1 << BIT_NUM);

**Clear a bit (turn it to 0):**
REG &= ~(1 << BIT_NUM);

**Toggle a bit (flip it):**
REG ^= (1 << BIT_NUM);

**Check a bit (test if it is 1):**
if (REG & (1 << BIT_NUM))

### DDRx (Data Direction Register)

Determines if a pin is an Input or an Output.

- `0` = **Input** (Read from the outside world)
- `1` = **Output** (Drive voltage to the outside world)

### PORTx (Data Register)

Its function changes depending on the DDRx state:

- **If pin is Output (DDR=1):**
    - `1` = Drives Pin HIGH (Vcc, e.g., 5V or 3.3V)
    - `0` = Drives Pin LOW (GND, 0V)
- **If pin is Input (DDR=0):**
    - `1` = **Enables** the internal pull-up resistor (defaults pin to HIGH).
    - `0` = **Disables** the pull-up resistor (pin is floating/High-Z).

### PINx (Input Pins Address)

Used to _read_ the actual, physical electrical state of the pin.
- Reads `1` if the physical pin is HIGH.
- Reads `0` if the physical pin is LOW.


## 5. Hardware Interfacing Logic

### Push Buttons
- **Configuration:** Typically connected between the microcontroller pin and Ground, with an internal or external **Pull-Up Resistor** enabled.
- **Not Pressed:** The pull-up resistor pulls the voltage HIGH. `PINx` reads **`1`**.
- **Pressed:** The button connects the pin directly to Ground. `PINx` reads **`0`**.

### LEDs
- **Active-Low (Connected to Voltage Rail):** The LED's anode is at Vcc, and the cathode is at the MCU pin.
    - To turn ON: Pin must be an Output (`DDR=1`) and driven LOW (`PORT=0`) so current can flow to ground.
- **Active-High (Connected to Ground):** The LED's cathode is at GND, and the anode is at the MCU pin.
    - To turn ON: Pin must be an Output (`DDR=1`) and driven HIGH (`PORT=1`).