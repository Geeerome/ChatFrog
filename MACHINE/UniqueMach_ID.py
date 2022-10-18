import socket

#GETS THE NAME OF THE MACHINE


def getMachineId():
    ident = socket.getfqdn()
    if len(ident) == 0 or ident == "localhost":
        ident = uuid.uuid1().hex
    print(ident)
    return ident 


getMachineId()