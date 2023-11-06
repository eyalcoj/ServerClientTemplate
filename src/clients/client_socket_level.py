import socket
from abc import ABC, abstractmethod

from src import protocols
from src.protocols import PackageType

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


class Client_socket_level(ABC):
    def __init__(self):
        self.data = None
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client.connect(ADDR)

    def send_data(self, data, packageType: PackageType):
        protocols.send_package(data, self.__client, packageType)
        print(f"[SEND_DATA] Client send to {SERVER}: {data}")

    def receive_data(self, conn):
        data = protocols.receive_package(conn)
        # TODO: להבין למה זה עושה מלא "None"
        if data is not None:
            self.data = data
            print(f"[RECEIVE_DATA] Client receive from {SERVER}: {self.data}")

    @abstractmethod
    def handle_data(self):
        pass
