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
    return var

def compose_header(version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress):
    """Takes the values to be filled into the IPv4 header
       and returns a 20-byte bytearray of the standard IPv4 header.
       Raises an appropriate ValueError if a parameter is erroneous.
    """

    # base case
    if version != 4:
        raise ValueError("version field must be 4")

    # assign string representation, variable's value, max bits for each variable.
    # This allows us to make an easy for loop for error codes.
    total_sizes = [
    ('tosdscp', tosdscp, 6), 
    ('totallength', totallength, 16),
    ('identification', identification, 16),
    ('flags', flags, 3),
    ('fragmentoffset', fragmentoffset, 13),
    ('timetolive', timetolive, 8),
    ('protocoltype', protocoltype, 8),
    ('headerchecksum', headerchecksum, 16),
    ('sourceaddress', sourceaddress, 32),
    ('destinationaddress', destinationaddress, 32)
    ]
    
    # check sizes for all values,
    # If the value given is less than 0 or the value is greater than when its
    # bitshifted, 
    for name, value, bit in total_sizes:
        if value < 0 or value >= (1 << bit):
            i = (1 << bit)
            raise ValueError(f"{name} value cannot fit in {bit} bits")
    

    # create Byte Array 
    header = bytearray(hdrlen * 4)
    
    header[0] = (version << 4) | hdrlen
    header[1] = (tosdscp << 2)
    
    header[2] = (totallength >> 8) & 0xFF
    header[3] = totallength & 0xFF

    header[4] = (identification >> 8) & 0xFF
    header[5] = identification & 0xFF

    flags_frag = (flags << 13) | fragmentoffset
    header[6] = (flags_frag >> 8) & 0xFF
    header[7] = flags_frag & 0xFF
    
    header[8] = timetolive
    header[9] = protocoltype
    
    header[10] = (headerchecksum >> 8) & 0xFF
    header[11] = headerchecksum & 0xFF
    
    header[12] = (sourceaddress >> 24) & 0xFF
    header[13] = (sourceaddress >> 16) & 0xFF

    header[14] = (sourceaddress >> 8) & 0xFF
    header[15] = sourceaddress & 0xFF
    
    header[16] = (destinationaddress >> 24) & 0xFF
    header[17] = (destinationaddress >> 16) & 0xFF

    header[18] = (destinationaddress >> 8) & 0xFF
    header[19] = destinationaddress & 0xFF

    return header

def compose_packet(hdrlen, tosdscp, identification, flags, fragmentoffset, timetolive, protocoltype, sourceaddress, destinationaddress, payload):
    """Takes the values to be filled into the IPv4 header
       and also a bytearray containing the payload.
       Returns a bytearray of the entire IPv4 packet (header and payload).
       Raises an appropriate ValueError if a parameter is erroneous.
    """
    totallength = hdrlen * 4 + len(payload)

    if  hdrlen < 5 or hdrlen > 15:
        raise ValueError("hdrlen must be at least 5 and no greater than 15")

    
    header = compose_header(
        4,
        hdrlen,
        tosdscp,
        totallength,
        identification,
        flags,
        fragmentoffset,
        timetolive,
        protocoltype,
        0,
        sourceaddress,
        destinationaddress
    )

    checksumhead = checksum(header)

    header[10] = (checksumhead >> 8) & 0xFF
    header[11] = checksumhead & 0xFF

    return header + payload
