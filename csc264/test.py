def avg_trials_from_ber(bit_error_probability, packet_length_b):
    p = bit_error_probability
    l = packet_length_b
    return 1.0 / ((1.0 - p) ** l)

print(f"{avg_trials_from_ber(0.001, 2000):.3f}")

# Same setup as in the previous question. If we call your result from the previous question P, 
# then P can be interpreted as the packet error probability or packet loss probability 
# (or more precisely: the probability that at least one bit in the packet is incorrect). 
# 
# 
# Suppose a transmitter wants to transmit a packet with L bits to a receiver and carries out retransmissions until successful
# (the transmitter always receives reliable feedback from the receiver about the transmission outcomes). 
# 
#
# Find an expression for the average number of transmission trials in terms of the packet length L (in bits) 
# and the bit error probability p and implement it in the Python function below. You will need the result from an earlier question.