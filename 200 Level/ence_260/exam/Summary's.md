
## Week 2 Summary

 **Understand the Sub components of a CPU**
- **ALU**: Actually performs the operations required, and in doing so generates the data that can be used in subsequent operations.
- **General purpose registers:** Physically close to the ALU, providing memory for the inputs to, and outputs from the ALU.
- **Control/Execute Unit:** Responsible for controlling the data flow to and from the general pupose registers and acts as a finite state machine in decoding the instructions from the program memory.
- **Control registers:** Stores metadata about the latest calculations

**Have an understanding of how the adder of an ALU is formed with logic gates**
- **Half Adders** are used to compare two individual bits with outputs sum and carry
- **Full Addders** use two half adders cascaded, Full adders themselves are cascaded to form a complete n-bit addition unit.

**Understand how the addition unit can be used to implement comparison behaviour.**
- **Addition and subtraction** can be implemented with the same addition circuit, provided two;s complement notation is ued for negative numbers.
- **Comparisons** can be achieved by using the Zero and Negative flags to determine which value is larger.
![[Pasted image 20261019150605.png]]
**Question:** Within which part of the computer architecture will this operation be performed, and how will the register be updated with the new value?

**Solution:** The operation will be performed within the CPU, specifically in the ALU. Therefore, the result has to leave the CPU and go back to the internal peripherals. The CPU will set the new value on the data bus, the address on the address bus (which confusingly uses a different address to perform a WRITE (0x0044) instruction that a READ (0x0024) instruction), and the control bus will indicate that it is performing a WRITE instruction:


**Decoder**
- Decodes a sequence, into a single logic variable.
**Encoder**
- Encodes a single input and converts, into a sequence (from total truth table, to truth statement)
**Multiplexer**
- Takes in 2 options and a switch, the switch flicks between the options forcing one at a time. Allows signals from different places, through to the same place
**Demux**

![[Pasted image 20261019120345.png]]

## Week 3 Summary

**The bidirectionality(I/O) of the pins is controlled using electrical signals.** To understand the oerall schematic we will need to conceptually understand the tristate buffer:![[Pasted image 20261019201134.png]]

A high impedance (Hi-Z) state is desirable because it means that it will not interfere with anything connected to B.

**Internal Pull-Up Resistors:** A pin that is not definitively connected to a specific state (for digital signals this means either 0 or 1) is said to be floating. Physically, these connections act as tiny antennae, and pick up electromagnetic interference from anything. The **internal pullup resistor** ensures that is is a constant 1.

**Shift Registers:** Shift registers are when the output of one flip-flop is connected o the input to the next, with a common clock. Used for serial-parallel conversions

**Counters:** Counters use the inverted output of the flip-flop as the input. This therefore acts as a clock divider or prescaler. Multiple connected flip-flops form a ripple counter.

**Synchronous Counters:** Use additional circuitry to predict the next state of the system as a function of the current state

**Finite state machine:** Controls systems used to specify the state of the system
##### Peripherals



### Week 4

![[Pasted image 20261020192543.png|562]]



![[Pasted image 20261020192936.png]]


There are only 3 different types of instructions

1. Data transfe to send information to and from our GPR
2. Arithmetic (+ - & | etc.)
3. Branching (manipulation of our Program Counter (for 'if, 'while' etc.))


****
 


![[Pasted image 20261020193339.png]]


#### Assembly
