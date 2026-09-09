We discuss simple baseband transmission schemes
We will also investigate their behaviour over channels and see how propagation phenomena impact the received signal 
Caveat: All of the following is simplified for illustration purposes


#### NRZ Encoding
- " Non return to zero" are concerned with transmission of bits
- To each bit value (0 or 1) a voltage level is associated that is transmitted for a fixed amount of time called the symbol time
- The inverse of the symbol time is the symbol rate or baud rate 
- As we transmit only one bit of information per symbol time, the symbol rate equals bit rate
- **Bipolar:**  (1,-1,1,1,-1)
- **Unipolar:** (0,1,0,0,1,1)

#### Mary Signaling
- There is no reason to restric to just two voltage levels, We can map transmission groups of k bits to M = 2^k different voltage levels. We use M different voltages
- If you use more M the error rate increase's

#### Attenuiation 
- The signal strength decays over distance where n = Ptx/Prx
- Ptx = ratio of the signal power observed at the output of the transmitter
- Prx = signal power observed at the input of the receiver

In many applications, these factors η can reach large values. Communications engineers have adopted the convention dB and the convertion is ηdB = 10 · log10 η
	- η = 10: we get ηdB = 10
	- η = 100: we get ηdB = 20
	- η = 1,000: we get ηdB = 30
#### Noise 

and **noise** are the main impairments of a baseband encoding