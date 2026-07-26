def payload(packet):
    """Takes a single bytearray parameter (representing an IPv4 packet)
       and returns just the packet's payload (as a bytearray).
    """
    hdr_len = packet[0] & 0x0F
    return packet[(hdr_len * 4):]