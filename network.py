#Todo:
#exit at welcome screen by pressing cursors

# Server = Player 1
# Client = Player 2

# Was wird uebertragen

#BEI VERBINDEN
#game TYPE
#random
#fixed power
#bounce
#invisible
#anzahl der runden
#beretis absovierte runden
#shot timeout


# JEDE tastaturaenderung
# player:
# aktueller spieler - deaktiviere eingabe fuer den jeweils anderen
# punkte fuer beide spieler
# winkel und speedpfeil fuer aktives raumschiff
# treffer - NEIN wertet jedes spiel selbst aus

#JEDE RUNDE
# planet:
# radius
# position planet
# masse
# evtl. n (textur des planetet)
# pos player 1 und 2

from socket import *
import pickle

class Network:
    def __init__(self, port, host = None, buf_size = 4096):
        self.s = socket(AF_INET, SOCK_DGRAM)
        self.addr = (host, port)
        self.buf_size = buf_size


    def wait_for_cnct(self):
        data = None
        self.s.bind(("", self.addr[1]))

        while data != "verbinde":
            (data, self.addr) = self.s.recvfrom(self.buf_size)
#            print("%s: %s" % (self.addr, data))

        self.s.sendto("verbunden", self.addr)

    def cnct(self):
        data = None

        while data != "verbunden":
            self.s.sendto("verbinde", self.addr)
            (data, recvaddr) = self.s.recvfrom(self.buf_size)
#            print("%s: %s" % (self.addr, data))


    def send(self, data):
        pdata = pickle.dumps(data)
        n = self.s.sendto(pdata, self.addr)
        print(data)
        return (True if n == len(pdata) else False)

    def recv(self):
        (data, recvaddr) = self.s.recvfrom(self.buf_size)
        print(pickle.loads(data))
        return pickle.loads(data)

    def __del__(self):
        self.s.close()




