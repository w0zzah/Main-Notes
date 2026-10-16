def destination_address(packet):
    """Takes a single bytearray parameter (representing an IPv4 packet)
       and returns a tuple (addr, dd), where: 
       - addr is the 32-bit value of the destination address
       - dd is a string in dotted decimal notation.
    """

    p1 = packet[16]
    p2 = packet[17]
    p3 = packet[18]
    p4 = packet[19]

    addr = (p1 << 24) + (p2 << 16) + (p3 << 8) + p4
    dd = str(p1) + "." + str(p2) + "."+ str(p3) + "." + str(p4)
    return addr, dd