import socket
from src.pype.utils.Logger import Logger
import time
import sys

class SourceInterface(object):

    protocol = 0
    buff_type = Buffer
    connection_timeout = 30


class Interface(object):

    motd = "A Mineraft server"
    max_players = 20
    compression_threshold = 256
    players = None

    def __init__(self):
        self.players = set()



    def open_socket(self, ip = "0.0.0.0", port = 19132):
        s = socket.create_connection((ip, port), 0)
        #bind = s.bind((ip, port))
        if not bind:
            Logger.critical("Couldn't bind to " + ip + ":" + str(port))
            exit()
