## Week 3 - Control

The control and execute unit is a **finite state machine (FSM)**. On each clock tick it moves to the next state, and the cycle repeats forever, which is how a program runs. The states go from **Fetch -> Decode -> Execute.** 
1. **Fetch** gets the instructions
2. **Decode** sets up the control signals
3. **Execute** runs the instructions over the set up control signals and stores the result in a destination


#### Fetch: 
Retrieves an instruction from the program memory
1. CPU gets the address held in the PC
2. Puts that address on the bus and reads the instruction from program flash (program memory)
3. The 16 bit opcode is latched into the instruction register

![[Pasted image 20261020201132.png]]

#### Decode:
- *Informs the control and execute unit how to configure the rest of the cpu, and the address / control busses*
1. The control unit examies the opcode bits and works out what the instruction is and which registers or addresses it uses.
2. Then configure the datapath
	- Which registers feed the ALU?
	- Which operation is selected?
	- Is the data bus read or written?
	- Where does the result go


![[Pasted image 20261020201146.png]]


#### Execute:

- Runs the instructions along the configured path

![[Pasted image 20261020201230.png]]

## Instructions
- Stored within 16-bits as opcodes. Each opcode contains the specific sequence of 1s and 0s to specify the operation, as well as additional function parameters. (Stores memory/register addresses, and/or constants)

- **Opcode bits:** fixed patterns that identify the operation.
- **Operand bits:** variable fields holding register numbers, constants, or address offsets.


### 3 Different types of Instructions

#### Data transfer: 

|        Syntax         |      Operands      |     Operation     |
| :-------------------: | :----------------: | :---------------: |
|    load Rd memLoc     | Rd[0...31], memLoc | Rd <- mem[memLoc] |
| **Control Registers** |     **Opcode**     |     **Flags**     |
|   ProgramCounter++    |   (sets of 1s )    |     No Flags      |


|                         Syntax                         |      Operands       |                Operation                |
| :----------------------------------------------------: | :-----------------: | :-------------------------------------: |
|                         breq k                         |   -64 <= k <= 63    | Is result of CP, CPI, SUB, or SUBI = 0? |
|                 **Control Registers**                  |     **Opcode**      |                **Flags**                |
| PC <- PC + 1 (if Z = 0)<br>PC <- PC + k + 1 (if Z = 1) | 1111 00kk kkkk k001 |                  None                   |


|                         Syntax                         |      Operands       |                Operation                |
| :----------------------------------------------------: | :-----------------: | :-------------------------------------: |
|                         breq k                         |   -64 <= k <= 63    | Is result of CP, CPI, SUB, or SUBI = 0? |
|                 **Control Registers**                  |     **Opcode**      |                **Flags**                |
| PC <- PC + 1 (if Z = 0)<br>PC <- PC + k + 1 (if Z = 1) | 1111 00kk kkkk k001 |                  None                   |