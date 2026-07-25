


def checksum(header):
    # Check if the header is at least 20 bytes long
    if len(header) < 20:
        raise ValueError("Header is too short")
        
    # Check if the header length is a multiple of 4
    if len(header) % 4 != 0:
        raise ValueError("Header does not contain a multiple of 4 bytes")
        
    # Sum up the 16-bit words
    x = 0
    for i in range(0, len(header), 2):
        # Construct the 16-bit integ
        er from two big-endian bytes
        word = (header[i] << 8) + header[i+1]
        x += word
        
    # Fold the carry bits back into the lower 16 bits
    while x > 0xFFFF:
        lowest16 = x & 0xFFFF
        carry = x >> 16
        x = lowest16 + carry
        
    # Take the ones' complement of the final result
    # We use ~x & 0xFFFF to ensure it stays a 16-bit positive integer
    return ~x & 0xFFFF

- **Validation Checks:** It first ensures the `bytearray` is at least 20 bytes long and is a multiple of 4, throwing the exact `ValueError` exceptions requested.
    
- **Big-Endian Extraction:** A `for` loop iterates through the bytearray with a step of 2. `header[i] << 8` grabs the first byte and shifts it 8 bits to the left (making it the most significant byte), and we add `header[i+1]` (the least significant byte) to create a single 16-bit integer.
    
- **Folding the Carry:** When you add 16-bit numbers, the sum can easily exceed 16 bits ($65535$ or `0xFFFF`). The `while` loop strips off the carry (any bits beyond the 16th position) and adds them back to the lowest 16 bits. It repeats this until the sum fits entirely within 16 bits.
    
- **Ones' Complement:** Because Python handles integers with arbitrary precision, a simple bitwise NOT `~x` on a positive number results in a negative number (e.g., `~0` is `-1`). By using `~x & 0xFFFF` (or `0xFFFF - x`), we restrict the complement strictly to the 16-bit boundaries, giving the correct positive integer.




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