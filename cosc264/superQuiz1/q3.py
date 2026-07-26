def checksum(header):
    if len(header) < 20:
        raise ValueError("head")
    if len(header) % 4 != 0:
        raise ValueError("4mod")

    x = 0
    for i in range(0, len(header), 2):
        word = (header[i] << 8) + header[i + 1]
        x += word

    while x > 0xFFFF:
        lowest16 = x & 0xFFFF
        carry = x >> 16
        x = lowest16 + carry

    var = ~x & 0xFFFF
    return var

def basic_packet_check(packet):
    """Takes a single bytearray parameter (representing an IPv4 packet)
       and returns True if it passes all the basic correctness checks.
       Raises an appropriate ValueError if any of the correctness checks fail.
    """

    if len(packet) < 20:
        raise ValueError("Packet does not contain a full IP header")

    version = packet[0] >> 4
    if version != 4:
        raise ValueError("Packet version number must equal 4")

    header_len = packet[0] & 0x0F
    if header_len < 5:
        raise ValueError("Packet hdrlen field must be at least 5")

    header_length_bytes = header_len * 4
    if len(packet) < header_length_bytes:
        raise ValueError("Packet does not contain a full IP header")

    total_length = (packet[2] << 8) + packet[3]
    if total_length != len(packet):
        raise ValueError("Packet totallength field is inconsistent with the packet length")

    header = packet[:header_length_bytes]
    if checksum(header) != 0:
        raise ValueError("Packet checksum failed")

    return True