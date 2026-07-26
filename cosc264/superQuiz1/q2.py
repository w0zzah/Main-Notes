def checksum(header):
    if len(header) < 20:
        raise ValueError("Header is too short")
    
    if len(header) % 4 != 0:
        raise ValueError("Header does not contain a multiple of 4 bytes")
    
    x = 0
    for i in range(0, len(header), 2):
        word = (header[i] << 8) + header[i + 1]
        x += word


    while x > 0xFFFF:
        lowest16 = x & 0xFFFF
        carry = x >> 16
        x = lowest16 + carry
        
    var = ~x & 0xFFFF

    return(var)