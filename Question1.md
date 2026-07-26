
  

while x > 0xFFFF:

lowest16 = x & 0xFFFF

carry = x >> 16

x = lowest16 + carry

var = ~x & 0xFFFF

  

return(var)

  
  

# A header whose checksum has not been set yet (The result of the

# function call is the value the checksum field should be set to.)

# empty_checksum_header = bytearray([0x45, 0x0, 0x0, 0x1e, 0x4, 0xd2, 0x0, 0x0, 0x40, 0x6, 0x0, 0x0, 0x12, 0x34, 0x56, 0x78, 0x98, 0x76, 0x54, 0x32])

# print(checksum(empty_checksum_header))

  

# A valid header should evaluate to 0.

# header1 = bytearray([0x45, 0x0, 0x0, 0x1e, 0x4, 0xd2, 0x0, 0x0, 0x40, 0x6, 0x20, 0xb4, 0x12, 0x34, 0x56, 0x78, 0x98, 0x76, 0x54, 0x32])

# print(checksum(header1))

  

def basic_packet_check(packet):

# 2. Check version number (highest 4 bits of the first byte)

version = pkt[0] >> 4

if version != 4:

raise ValueError("Packet version number must equal 4")

ihl = pkt[0] & 0x0F

if ihl < 5:

raise ValueError("Packet hdrlen field must be at least 5")

header_length_bytes = ihl * 4

if len(pkt) < header_length_bytes:

raise ValueError("Packet does not contain a full IP header")

# 4. Check total length (bytes at index 2 and 3)

total_length = (pkt[2] << 8) + pkt[3]

if total_length != len(pkt):

raise ValueError("Packet totallength field is inconsistent with the packet length")

# 5. Check the header checksum

# (Extract only the header bytes using the calculated header length)

header = pkt[:header_length_bytes]

if checksum(header) != 0:

raise ValueError("Packet checksum failed")

if len(packet) < 20:

raise ValueError("Packet does not contain a full IP header")

version = packet[0] >> 4

if version != 4:

raise ValueError("Packet Version Number must equal 4")

  

hdrlen = packet[0] & 0x0F

  
  

if hdrlen < 5:

raise ValueError("Packet hdrlen field must be at least 5")

  

if checksum(packet[:8]) == 0:

raise("Packet checksum failed")

ttlen = packet[3] + packet[4]

if ttlen != len(packet):

raise ValueError("Packet totallength field is inconsistent with the packet length")

  

else:

return True

  

pkt1 = bytearray([0x45, 0x0, 0x0, 0x1e, 0x4, 0xd2, 0x0, 0x0, 0x40, 0x6, 0x20, 0xb4, 0x12, 0x34, 0x56, 0x78, 0x98, 0x76, 0x54, 0x32, 0x0, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09])

print(basic_packet_check(pkt1))