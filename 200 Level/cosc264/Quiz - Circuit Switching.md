**Propagation delay:** The time it takes for a signal to travel from the sender to the receiver or from input to the output of the circuit. This can be determined by the physical **Distance** or the **speed** of the signal through the medium.

**Transmission Delay:** The time needed to push all bits of data onto a comm link and is determined by packets size and bandwidth. independent of propagation delay.

**Processing delay:** the time a route takes to examine a packets header before sending.

**Standard Procedure:** Propagation ->  Transmission -> Processing -> Propagation etc.

### Writing in code: 
```python

def connection_setup_delay(med_len, speed, msg_length, data_rate, proc_time)
	totalSpeed = (med_len) / (data_rate)
	totalProcessingTime = proc_time * 4
	
```


Propagation delay is like the time it takes for *just the head* of a train to travel from a to b.

Transmission delay is like the time it would take if you were standing still for the trains to fully pass you (the time between the head a the tail passing a stationary observer).