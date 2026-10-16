def checkLen(argv):
    return len(argv) != 4
#      Check port's are not the same
def portsEqual(ports):
    return ports[0] == ports[1] or ports[1] == ports[2] or ports[2] == ports[0]:

def setup():
    try:
        ports = [argv[0], argv[1], argv[2]]
        if checkLen(argv):
            raise IndexError
        if portsEqual(ports):
            raise TypeError
        if 
    except IndexError:
        print("ERROR: Incorrect number of command line arguments")
        exit()