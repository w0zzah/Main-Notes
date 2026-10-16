# Server python file for sockets programming 
from socket import socket, AF_INET, SOCK_DGRAM
from sys import argv, exit
from datetime import datetime
from select import select

# constants
PACKET_TYPE = 0x0001
REQUEST_DATE = 0x0001
REQUEST_TIME =  0x0002
HOST = "localhost"

LANGUAGE_NAMES = {
     "English" : 0x0001,
     "Māori" : 0x0002,
     "German" : 0x0003
}

MONTHS = {
    'English': ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    'Māori': ["Kohi-tātea", "Hui-tanguru", "Poutū-te-rangi", "Paenga-whāwhā", "Haratua", "Pipiri", "Hōngingoi", "Here-turi-kōkā", "Mahuru", "Whiringa-ā-nuku", "Whiringa-ā-rangi", "Hakihea"],
    'German': ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
}


def dt_request_check(packet):
    if len(packet) != 6:
        print("ERROR: Packet length incorrect for a DT_Request, dropping packet")
        return None

    if 0x36FB != (packet[0] << 8 | packet[1]):
        print("ERROR: Packet magic number is incorrect, dropping packet")
        return None

    if PACKET_TYPE != (packet[2] << 8 | packet[3]):
        print("ERROR: Packet is not a DT_Request, dropping packet")
        return None
        
    request_type = packet[4] << 8 | packet[5]
    if request_type not in [REQUEST_DATE, REQUEST_TIME]:
        print("ERROR: Packet has invalid type, dropping packet")
        return None

    return request_type

def dt_response(language, now, text_bytes):
    length = len(text_bytes)
    packet = bytearray(13 + length)
    lang = LANGUAGE_NAMES[language]
    packet[0] = 0x36
    packet[1] = 0xFB
    packet[2] = 0x00
    packet[3] = 0x02
    packet[4] = (lang >> 8) & 0xFF
    packet[5] = lang & 0xFF
    packet[6] = (now.year >> 8) & 0xFF
    packet[7] = now.year & 0xFF
    packet[8] = now.month
    packet[9] = now.day
    packet[10] = now.hour
    packet[11] = now.minute
    packet[12] = length
    packet[13:] = text_bytes
    return packet

def create_reply(request_type, language, now):
    month_name = MONTHS[language][now.month - 1]
    
    if language == 'English':
        if request_type == REQUEST_DATE:
            return f"Today's date is {month_name} {now.day}, {now.year}"
        else:
            return f"The current time is {now.hour:02}:{now.minute:02}"
    
    elif language == 'Māori':
        if request_type == REQUEST_DATE:
            return f"Ko te rā o tēnei rā ko {month_name} {now.day}, {now.year}"
        else:
            return f"Ko te wā o tēnei wā {now.hour:02}:{now.minute:02}"
    
    elif language == 'German':
        if request_type == REQUEST_DATE:
            return f"Heute ist der {now.day}. {month_name} {now.year}"
        else:
            return f"Die Uhrzeit ist {now.hour:02}:{now.minute:02}"

def check_len(arguments):
    return len(arguments) != 4

def ports_equal(ports):
    return ports[0] == ports[1] or ports[1] == ports[2] or ports[2] == ports[0]


def setup():
    try:
        # ------------------------------------------------------------- test1
        if check_len(argv):
            raise IndexError
            
        raw_ports = [argv[1], argv[2], argv[3]]

        if ports_equal(raw_ports):
            print("ERROR: Duplicate ports given")
            exit(1)
            
        ports = []
                #  ------------------------------------------------------------ test2
        for port_str in raw_ports:
            try:
                port = int(port_str)
            except ValueError:
                #  ------------------------------------------------------------ test3
                print(f"ERROR: Given port '{port_str}' is not an integer")
                exit(1)
                
                #  ------------------------------------------------------------ test4
            if not (1024 <= port <= 32767):
                print(f"ERROR: Given port '{port_str}' is not in the range [1024, 32767]")
                exit(1)
    
            ports.append(port)

    except IndexError:
        print("ERROR: Incorrect number of command line arguments")
        exit(1)

    return ports


def bind_sockets(ports):
    # Could use tuples or library?
    sockets = []
    names = ["English", "Māori", "German"]

    for name, port in zip(names, ports): # Zip is fucking cool man
        print(f"Creating socket for {name}")
        try:
            sock = socket(AF_INET, SOCK_DGRAM)

        except OSError:
            print(f"ERROR: Socket creation failed")
            for sock in sockets:
                sock.close()
            exit(1)
        print(f"Binding to port {port}")
        try:
            sock.bind((HOST, port))

        except OSError:
            print("ERROR: Socket binding failed")
            sock.close()
            for sock in sockets:
                sock.close()
            exit(1)

        sock.settimeout(1)
        sockets.append(sock)    

    return sockets


def main():
    ports = setup()
    sockets = bind_sockets(ports)
    langs = ["English", "Māori", "German"]

    try: 
        while True:
            print("Waiting for requests...")
            read, _, _ = select(sockets, [], [])
            for sock in read:
                index = sockets.index(sock)
                language = langs[index]
                try:
                    packet, client_address = sock.recvfrom(300)
                except TimeoutError:
                    print("ERROR: Receiving timed out, dropping packet")
                    continue
                except OSError:
                    print("ERROR: Receiving failed, dropping packet")
                    continue

                request_type = dt_request_check(packet)
                if request_type is None:
                    continue

                ip_address = client_address[0]
                req_name = "date" if request_type == REQUEST_DATE else "time"
                print(f"{language} received {req_name} request from {ip_address}")


                now = datetime.now()
                text = create_reply(request_type, language, now)
                text_bytes = text.encode("utf-8")

                if len(text_bytes) > 255:
                    print("ERROR: Text too long, dropping packet")
                    continue

                response = dt_response(language, now, text_bytes)
                try:
                    sock.sendto(response, client_address)
                except OSError:
                    print("ERROR: Sending failed, dropping packet")
                    continue
                
                print("Response sent")
    finally:
        for sock in sockets:
            sock.close()
        
        
main()