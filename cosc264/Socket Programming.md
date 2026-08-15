Basic Ip service is packet delivery:
- Does not require a connection or shared state
- Does not use acknowledgements
- There are no retransmissions
- There is no guarenteed in-sequence delivery
An IPv4 address corresponds to the street address of a house and the port numebr refers to an individual person in that house.

An IPv4 address refers to the end host and the port number is a particular app or server soft that is running in that end host

### Processes can be in one of several states (Runnable -> Running -> Blocked)
- Running: actually running on the processor 
- Runnable: ready to run on a processor, but currently not doing so 
- Blocked: process is waiting for input from a hard disk / socket / . . .
	- when input arrives the process becomes runnable or running 
	- while blocked, the process does not use any CPU cycles

# Client:
- The client runs on the end host
- Knows servers IP add / port number and needs  to have its own IP / port number with a socket bound to these
- Initiates contact with tthe server through the socket that binds them
- After binding the client application can end


# Server
- Runs on the end host
- Needs an IP that is known to clients
- Accept service reqs from clients & responds
- Run all the time to support several clients


# TCP Client:
## Flow
**Socket** -> Create a socket, this allocates resources and assigns a random unused port number

**Connect** -> Establish connection with server

**recv/read/send/write** -> Altering socket
**close** -> Closes connection

# TCP Server:
## Flow
**Socket** -> Create a socket, this allocates resources and assigns a random unused port number

**Bind** -> Bind a socket to a particular port number and IP
**Listen** -> Declare willingness to accept incoming conenctions, allocate resorces for incoming connection requests
**Accept** -> Accept an incoming connection request, and create a new socket for this connection bound to the same port as the socket created by listen

**recv/read/send/write** -> Altering socket
**close** -> Closes connection

# UDP Client:
## Flow
**Socket** -> Create a socket, this allocates resources and assigns a random unused port number

**recvfrom() / sendto()** -> interaction

**close** -> Closes connection

# UDP Server:
## Flow
**Socket** -> Create a socket, this allocates resources and assigns a random unused port number

**Bind** -> Bind a socket to a particular port number and IP
**Listen** -> Declare willingness to accept incoming conenctions, allocate resorces for incoming connection requests
**Accept** -> Accept an incoming connection request, and create a new socket for this connection bound to the same port as the socket created by listen

**recv/read/send/write** -> Altering socket
**close** -> Closes connection


### Sockets():
- A socket is bound to exactly one port
- A socket is associated with an underlying protocol
- A socket has a buffer
- Type TCP -> SOCK_STREAM
- Type UDP -> SOCK_DGRAM

```python
from socket import socket 
# a TCP client 
# get the address of a TCP server 
address = (address_ipv4, port)
# create a socket s 
s = socket (AF_INET, SOCK_STREAM) 
# connect the socket to address of a TCP server 
s.connect(address)
# prepare a message msg, e.g. as bytearray
...
# send the message to the TCP server 
amount = s.send(msg)
# receive a response from the server
resp = s.recv(4096)
# link(bind) the socket to address 
s.bind(address)
#start listening
s.listen(5) 
```

# Sockets:

### Stream Sockets:
- Reliable in-sequence delivery of a byte-stream
- used with TCP
- If delivery fails, the sending app is notified
### Datagram sockets:
- Offers delivery of distinct finite-sized datagrams
- Does not guarantee reliable or in-sequence delivery
- Often used with UDP protocol
- If delivery fails the sending application is not informed
### Raw Sockets:
- bypass UDP & TCP to directly send IP packets
### Sequenced-packet Sockets:
- Variant of a stream socket 

# Socket CMDS
w
	**send()** or **write()** -> Sending data
	**recv** or **read()** -> Reading data
	s.**connect**(address) -> Connecting **address** -> A yuple containg (address_ipv4, port)
	Raises a socket.**gaierror** when an address error occurs (Slide 38)
	**Select():**
	Waits for input on one or more sockets (e.g Incoming Packets) -> IF no input is available at time of call then it is put into a blocked state. 
	**Send():**
	- For all these functions the data that is to be sent is supplied in the bytes parameter, being a bytes or bytearray object
	- Requires that the addresse has been specified before calling the sockets conenct() method
	 **recv() & recvfrom():**
	- Return data and address as bytes
	 **bind(address_ipv4, port):**
	- Links the socket to a particular IP / port num
	- address_ipv4 is the string of the hostname or IP in dotted-decimal notation and the port is an integer. 
	**listen(backlog)** -> Listen's for incoming data with the total length = backlog 
	**accept()** -> Waits for an incomming connection requests **TCP Only**
	- accept returns values for **Conn**(socket where you can access new connection) & **address** (the address information about the requesting client) 
	**close** -> Called when you do not need a socket, will give the socket back resources


```python
from socket import socket, AF_INET, SOCK_STREAM

# 1. Prepare the server address (host, port) and create the TCP socket
address = ('127.0.0.1', 8080)  # Example address
server_socket = socket(AF_INET, SOCK_STREAM)

# 2. Bind the socket to the address and start listening for connections
server_socket.bind(address)
server_socket.listen(5)
print("Server is listening for incoming connections...")

while True:
    # 3. Accept an incoming client connection
    # - conn: A new socket object used to communicate with the client
    # - client_addr: The IP address and port of the connected client
    conn, client_addr = server_socket.accept()
    print(f"Connected to client at: {client_addr}")

    try:
        # 4. Receive data from the client (buffer size of 4096 bytes)
        msg = conn.recv(4096)
        print(f"Received message: {msg.decode('utf-8')}")

        # 5. Prepare and send the response back to the client
        resp = b"Hello from the server!"  # Example response bytes
        conn.send(resp)

    finally:
        # 6. Always close the connection when done
        conn.close()
```


### Socket communicating locally is through 127.0.0.1, known as 'localhost'

### Convert from host to network
```python
from socket import htonl, htons, ntohl, ntohs 
netlong = htonl(hostlong) 
netshort = htons(hostshort) 
hostlong = ntohl(netlong) 
hostshort = ntohs(netshort)
```
- throw **OverflowErrors** if given value can't fit in 16/32bits

### Get Address info 
```python
from socket import getaddrinfo

services = getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)
host = "domain name / str representation of apv4 address"
port = "a port no. or string service name"
```
- Raises a **socket.gaierror** if the host cannot be found or the specified service isn’t available for the host.