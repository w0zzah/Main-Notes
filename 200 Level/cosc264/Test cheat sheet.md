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


When a new packet arrives, If no packet is transmitting, then the new packet is started immediately and the waiting time of the packet is **zero**.

Else the packet is sent to the end of the queue. The waiting time for the packet is the **remaining time** for the packet **currently in transmission** **PLUS** the **transmission times of all packets ahead** in the queue.