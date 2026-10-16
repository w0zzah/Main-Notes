**Network Delays & Formulas**

| **Delay Type**   | **Formula / Concept**                                      | **Key Detail**                                                                                                      |
| ---------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Propagation**  | $\frac{\text{Distance}}{\text{Speed}}$                     | Depends only on the physical medium length and signal speed.                                                        |
| **Transmission** | $\frac{\text{Packet Size (bits)}}{\text{Link Rate (bps)}}$ | Convert Bytes to bits ($\times 8$) before dividing by bits per second (bps).                                        |
| **Queueing**     | $\text{Remaining Tx} + (n \times \text{Full Tx})$          | Remaining Tx of current packet (avg 0.5) + full Tx time of $n$ queued packets.                                      |
| **Pipelining**   | $\text{First Pkt Delay} + (n - 1) \times \text{Tx}$        | First packet incurs full path delay (Trans + Prop + Proc). Subsequent packets arrive separated by one link Tx time. |

**Socket Programming**

| **Concept / API** | **Function**                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| `ntohl()`         | Converts 32-bit (Long) from **N**etwork to **H**ost byte order.            |
| `SOCK_STREAM`     | TCP. Reliable, in-sequence, connection-oriented stream of bytes.           |
| `SOCK_DGRAM`      | UDP. Unreliable, connectionless, preserves message boundaries.             |
| `accept()`        | Returns a **new socket** (for the client) + the **client's address**.      |
| `recvfrom()`      | Reads exactly **one discrete packet** per call, regardless of buffer size. |

**Physical Layer: Modulation & Line Coding**

  

- **ASK (Amplitude):** Varies signal height (susceptible to noise).
- **FSK (Frequency):** Varies pitch/rate of waves (noise resistant, uses more bandwidth).
- **PSK (Phase):** Shifts starting angle of the wave (highly efficient).   
- **M-ary Transmission:** Number of bits per voltage level = $\lfloor \log_2(\text{Available Levels}) \rfloor$.
- **Manchester Encoding:** A transition always occurs in the exact **middle** of every bit interval.
- **NRZ:** Unipolar (0V and +V) vs. Bipolar (-V and +V).

**Data Link Layer & MAC Protocols**

  

- **Error Control:** Link-layer error control is for **efficiency** (fixes errors quickly over one link). Transport-layer error control is for **correctness** (end-to-end guarantee).
    
      
    
- **Pure ALOHA:** Transmits instantly. Vulnerable period is **$2 \times$ frame duration**.
    
      
    
- **CSMA (Carrier Sense):** 1-persistent and p-persistent wait if the channel is busy. Non-persistent senses, but if busy, waits a random time before sensing again.
    
      
    
- **FDMA:** Access delay is **0 seconds** because every station has a dedicated 24/7 frequency channel.
    
      
    
- **Ethernet Minimum Payload:** **46 bytes** (64 bytes total frame - 18 byte header). Required for CSMA/CD collision detection signals to propagate across the maximum cable length while the sender is still transmitting.
    
      
    

**Network Layer (IPv4 & Routing)**

  

- **"Hourglass Model":** IP over Everything (runs on any physical link), Everything over IP (supports any application).
    
      
    
- **IPv4 Properties:** Connectionless, 32-bit addresses, best-effort (unreliable), packets can arrive out of order.
    
      
    
- **Router Packet Processing:** 1) Strip Link header, 2) Verify IP checksum, 3) Decrement TTL (drop if $\le 1$), 4) Recalc checksum, 5) Forward lookup & encapsulate.
    
      
    
- **Forwarding Table:** Always uses **Longest Prefix Match** (the subnet mask with the most 1-bits wins).
    
      
    
- **Fragmentation:** Offset = Byte index of the payload. Reassembly happens **only at the final destination** because packets might take different paths, and reassembly at routers wastes CPU/buffer memory.
    
      
    
- **Subnetting Calculation:** Network Address = `IP_Address AND Subnet_Mask`.