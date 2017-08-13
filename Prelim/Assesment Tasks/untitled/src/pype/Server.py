from src.pype.utils.Terminal import Terminal
from src.pype.network.Interface import Interface


class Server(object):

    def __init__(self):
        super(Server, self).__init__()
        Terminal.init()
        self.interface = Interface()
