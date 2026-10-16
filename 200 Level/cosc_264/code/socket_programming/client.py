from socket import socket, getaddrinfo, gaierror, timeout, AF_INET, SOCK_DGRAM
from sys import argv, exit


# constants


# helper functions or classes

def setup(argv):
    if len(argv) != 4:
        print("ERROR: Incorrect number of command line arguments")
        exit(1)
    
    req_str = argv[1]
    if req_str not in ("date", "time"):
        print(f"ERROR: Request type '{req_str}' is not valid")
        exit(1)

    req_type = 0x0001 if req_str == "date" else 0x0002

    hostname = argv[2]
    port_str = argv[3]

    try:
        port = int(port_str)
    except ValueError:
        print(f"ERROR: Given port '{port_str}' is not an integer")
        exit(1)

    if not (1024 <= port <= 32767):
        print(f"ERROR: Given port '{port_str}' is not in the range [1024, 32767]")
        exit(1)

    try:
        addr_info = getaddrinfo(hostname, port, AF_INET, SOCK_DGRAM)
        _, _, _, _, sockaddr = addr_info[0]
        ip_addr, port = sockaddr        # Alternative ip_addr = addr_info[0][4][0]

    except gaierror:
        print("ERROR: Hostname resolution failed")
        exit(1)
    


    return req_type, ip_addr, port

def create_dt_req(req_type):
    packet = bytearray(6)
    packet[0] = 0x36FB >> 8 & 0xFF
    packet[1] = 0x36FB & 0xFF
    packet[2] = 0x0001 >> 8 & 0xFF
    packet[3] = 0x0001 & 0xFF
    packet[4] = req_type >> 8 & 0xFF
    packet[5] = req_type & 0xFF
    return packet


def dt_response_check(packet):
    if len(packet) < 13:
        print("ERROR: Packet is too small to be a DT_Response")
        return None

    magic = (packet[0] << 8) | packet[1]
    if magic != 0x36FB:
        print("ERROR: Packet magic number is incorrect")
        return None

    packet_type = (packet[2] << 8) | packet[3]
    if packet_type != 0x0002:
        print("ERROR: Packet is not a DT_Response")
        return None

    language = (packet[4] << 8) | packet[5]
    if language not in (0x0001, 0x0002, 0x0003):
        print("ERROR: Packet has invalid language")
        return None

    fields = dt_response_check_2(packet)
    if fields is None:
        return None

    year, month, day, hour, minute, text = fields

    return {
        "language": language,
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "minute": minute,
        "text": text,
    }


def dt_response_check_2(packet):
    year = (packet[6] << 8) | packet[7]
    if year >= 2100:
        print("ERROR: Packet has invalid year")
        return None

    month = packet[8]
    if not 1 <= month <= 12:
        print("ERROR: Packet has invalid month")
        return None

    day = packet[9]
    if not 1 <= day <= 31:
        print("ERROR: Packet has invalid day")
        return None

    hour = packet[10]
    if not 0 <= hour <= 23:
        print("ERROR: Packet has invalid hour")
        return None

    minute = packet[11]
    if not 0 <= minute <= 59:
        print("ERROR: Packet has invalid minute")
        return None

    length = packet[12]
    if len(packet) != 13 + length:
        print("ERROR: Packet text length is incorrect")
        return None

    try:
        text = packet[13:].decode("utf-8")
    except UnicodeDecodeError:
        print("ERROR: Packet has invalid text")
        return None

    return year, month, day, hour, minute, text
    

def main():
    # main function
    req_type, ip_addr, port = setup(argv)

    print("Creating socket")

    try:
        sock = socket(AF_INET, SOCK_DGRAM)
    except OSError:
        print("ERROR: Socket creation failed")
        exit(1)
        
    sock.settimeout(1)
    

    try:
        req_packet = create_dt_req(req_type)

        try:
            sock.sendto(req_packet, (ip_addr, port))
        except OSError:
            print("ERROR: Sending failed")
            exit(1)

        label = "Date" if req_type == 0x0001 else "Time"
        print(f"{label} request sent to {ip_addr}:{port}")

        try: 
            resp_packet, _ = sock.recvfrom(300)

        except timeout:
            print("ERROR: Receiving timed out")
            exit(1)

        except OSError:
            print("ERROR: Receiving failed")
            exit(1)

        fields = dt_response_check(resp_packet)
        if fields is None:
            exit(1)
        langs = ["English", "Māori", "German"]
        language_name = langs[fields["language"] - 1]
        # set language
        print(f"{language_name} response received:")
        print(f"Text: {fields['text']}")
        print(f"Date: {fields['day']}/{fields['month']}/{fields['year']}")
        print(f"Time: {fields['hour']:02}:{fields['minute']:02}")
    finally:
        sock.close()

main()