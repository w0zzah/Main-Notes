#### Networked applications

|    d     |    v     |       l       |     r     |       rout        |         n         |
| :------: | :------: | :-----------: | :-------: | :---------------: | :---------------: |
| Distance | Velocity | Packet Length | Data Rate | Number of Routers | Number of Packets |


$$d_{\text{prop}} = \frac{d}{v}$$
$$d_{\text{trans}} = \frac{l}{r}$$
$$d_{\text{queue}} = \left(0.5 \times \frac{L}{R}\right) \times n$$
$$\text{Total time through n routers} = \left(\left(d_{\text{prop}} + d_{\text{trans}} + d_{\text{process}}\right) \times rout \right) + d_{\text{prop}} + \left(d_{\text{trans} } \times n\right)$$
#### Packet Loss
- **Causes:** Network congestion forces devices to drop incoming packets, physical barriers and signal overlap disrupt wifi.

**Maths:**  $$P_{losing \space 1 \space bit:} = 1 - (1 - bit\space error \space rate)^{packet\space length}$$
$$Estimated \space Number \space of \space trials \space (for\space 1 \space packet) = \frac{1}{1 - P_{losing 1 bit}}$$
#### Part 2
|         |                                                                                           PACKET                                                                                            |                                                           CIRCUIT                                                            |
| :-----: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------: |
| General | data in packets, no reserved resources, packets may take different paths, better for bursty/variable traffic (VBR). Packet has header, payload and optional trailer (to detect and correct) |             fixed route, reserved resources,<br>good for constant bit rate (CBR)<br>communication over network)              |
|  PROS   |                                                                 Efficent use of bandwidth, routes around network congestion                                                                 |                                                Dedicated transmission channel                                                |
|  CONS   |                                                                    Packets can become lost, packets dont arrive in order                                                                    | Dedicated channels can cause delays if a channel is unavailable, Physical dedicatedlink between devices, requires call setup |
![[Pipelining diagram.jpg]]
### Layering and Reference Models


#### Part 3
##### Socket Types:
- **DGRAM:** Uses UDP. It is connectionless, unreliable and does not guarantee packet ordering or delivery. (Used for fast, low overhead communication)
- **SEQPACKET:** Provides reliable, sequenced data delivery like STREAM, but preserves record/packet boundaries rather than treating data as a continuous stream of bytes.
- **RAW:** Direct access to lower-level networking protocols like IP or ICMP. bypassing the transport of TCP or UDP Entirely
- **STREAM:** Reliable two way connection based byte stream. It uses TCP to ensure that data is transferred without loss, corruption or duplication

#### OSI:
1. **Physical:** Bit transmission, modulation, signal encoding, cables
2. **Data Link**: Framming MAC addressing, error detection
3. **Network:** IP routing, Path determination, logical addressing
4. **Transport:** End to end delivery, TCP/UDP segmentation
5. **Session:** Managing and terminating communication sessions between apps
6. **Presentation:** Data translation, encryption, compression, syntax formatting
7. **Application Layer:** Network services directly used by apps

### OSI
We **Format** the data from raw to digital form, then we compress it using **Source Coding** then we fix holes using **Channel Coding** where we finally convert it to waves using **Modulation.**

| **Feature**               | **ASK (Amplitude)**       | **FSK (Frequency)**  | **PSK (Phase)**             |
| ------------------------- | ------------------------- | -------------------- | --------------------------- |
| **Modulated Parameter**   | Signal height/power ($A$) | Rate of cycles ($f$) | Signal start angle ($\phi$) |
| **Noise Resistance**      | Low (poor)                | Moderate             | High (excellent)            |
| **Bandwidth Requirement** | Low                       | High                 | Low to Moderate             |
| **Circuit Complexity**    | Very Simple               | Moderate             | Complex                     |
| **Primary Advantage**     | Simplicity                | Error resistance     | High spectral efficiency    |

### Transmission:
##### M - ary:
- The number of voltage levels required for n bits is 2^n
- e.g for 3 bits you would need (000, 001, 010, 100, 011, 110, 101, 111) where each collection of 3 bits would need to be a unqiue voltage level.


#### Waveforms

##### ASK:

##### FSK:

##### PSK:
$$s_\text{i}(t) = \left (\sqrt \frac{2E_s}{T_s}\right) \times \left(\cos(2\pi f_c t + \theta _i\right)$$
#### FDMA

**Encapsulation:**



The concept of a Path MTU (Maximum Transmission Unit) boils down to finding the "weakest link" in a network route.

**The Networking Concept**

When you send data across the internet, it gets chopped into smaller chunks called packets. Every physical link (like an Ethernet cable, a Wi-Fi connection, or a VPN tunnel) has a maximum packet size it can handle, measured in bytes. This is its MTU.

As your packet travels from router to router, it must fit through every single link. If a packet is larger than a link's MTU, the router must either fragment (slice) it into smaller pieces—which slows down the network—or drop it entirely. Therefore, the **Path MTU** is simply the smallest MTU of any single hop along the entire route.

> Think of it like driving a delivery truck from New York to Los Angeles. Along the way, you have to pass under four bridges with height clearances of 15ft, 14ft, 12ft, and 15ft. The tallest truck you can drive the entire way without crashing is 12ft. The 12ft bridge dictates the "Path Clearance," just as the smallest link dictates the Path MTU.

**How the Python Code Works**

| **Code Segment**           | **What It Does**                                                                               | **Why It Matters**                                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `def path_mtu(link_mtus):` | Defines the function and accepts a single argument, which is expected to be a list of numbers. | It creates a reusable block of code where you can pass in any route's MTU data.                           |
| `if not link_mtus:`        | Checks if the provided list is empty. In Python, an empty list evaluates to `False`.           | Prevents the program from crashing if someone accidentally passes in an empty list of networks.           |
| `raise ValueError(...)`    | Manually triggers an error with a clear, readable message.                                     | Tells the user exactly _why_ the function failed, rather than throwing a confusing built-in Python error. |
| `return min(link_mtus)`    | Uses Python's built-in `min()` function to scan the entire list and return the lowest number.  | This is the mathematical equivalent of finding the "weakest link" or the lowest bridge clearance.         |