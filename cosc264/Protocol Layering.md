Networking software:
Structuring Principles organize networking software to achieve:
- Modularity and software re-use
- Independence of network technologies
- Seperation of concerns
- Correctness


**Layering**
- A key structuring principle for networking software is layering: the functionality is decomposed into a chain of layers so that later N offers services through an interface to layer N+1 and itself is only allowed to use service offered by layer N-1


### Layering Concepts:

#### Layering Interface & SAP
- A layer N offers an N-service interface -> eg the socket API
- The next higher layer N + 1 is only allowed to use the N interface, but not any of the lower interfaces, (eg n-1) this applies to all layers
- The N-interface offers services at service access points (SAP)
- The N-interface can offer several SAPs, this allows to multiplex between different layer  N+1 protcols or different layer N + 1 "Connections" or "Sessions"
- EXAMPLE sockets and their associated port numbers are SAP's

#### Layering Service & protocol
- The layer N-service is implemented through an N-protocol
- The N-protocol makes direct use of N-1 services
- The N-protocol makes no assumption whatsoever on what is on layer N + 1
- It exchanges protocol data units (PDUS) with a peer N-protocol entity - it constructs these PDUs itself and hands them over to its local N -1-layer to deliver them to peer N-protocol entity (which in turn receives it from its local N-1 layer)
- PDU is a more fancy word for a packet

#### Layout of a layer N PDU:
- The N-PDU is constructed by the N-protocol entity
- It carries the data handed over by layer N + 1 for transmission, also refered to as **user, data, payload** or as a service data uniy **N-SDU**
- The sending N protocol entity adds a N-protocol **header** for which it catties control infromation such as sequence numbers, addresses and flags that are important for the N-protocol but not recieving N + 1layer or N -1 layer
- It might furthermore add an N-protocol **trailer** (which is usually a checksum)
- The receiving N-protocol entity removes the nheader and  trailer and hands over the N + 1 data to its lcoal layer N + 1 entity

