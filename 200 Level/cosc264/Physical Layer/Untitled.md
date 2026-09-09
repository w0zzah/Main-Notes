
### Transmitting Digital data using analog signals
- Incomputers and communication networks we work primarily with binary data where mostr transmission data will only allow analog physical signals. 
- We have means to transmit analog wayforms over distance according to the digital data that we have.
- The process of imprinting data onto waveforms is called modulation

### Structure of Communication systems
- Data goes from the source to the formatt then sources encode then channel encode then modulator.
- Formatting -> Source Encoding -> Channel Encoding -> Modulator -> (Then reverse)
- Digital Symbols / Bits-------------------------------------------------(Then Analog)---(Then back to bits)

#### Formatting
- Converts source signal into the digital data form. e.g a video camera captures light and directs it onto an image sensor which generate a raw digital image represented as a finite number of pixels.

#### Source Coding
- Compression, is the encoding of digital data with the goal of reducing size
- **Lossless:** encoded in such a way where it can be perfectly resotred
- **Lossy:** The decoded data may differ as long as humans cannot percieve the diference

#### Channel Coding
- Channel encoding takes a stream of digital symbols / bits and adds redundant bits to counter the occurence of transmission errors.
- Adding redundancy can improve the receivers chance to guess the correct data even when the channel adds distortions.
- Can reduce the bit error probability

#### Modulator and Channel
- Modulator and channel takes a sequence of bits and maps each of those bits to a physical signal or waveform for a certain duration. 
- When we modulate the bits the zero bit will be mapped to some waveform s0(t) and the one bit will be mapped to another waveform s1(t)


### Summary
We **Format** the data from raw to digital form, then we compress it using **Source Coding** then we fix holes using **Channel Coding** where we finally convert it to waves using **Modulation.**