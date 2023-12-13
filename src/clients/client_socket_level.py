import socket
from abc import ABC, abstractmethod

from src.data_base import UserData
from src.protocols import protocol_socket_level
from src.protocols.protocol_socket_level import PackageType

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


class ClientSocketLevel:
    def __init__(self):
        self.__user_data = UserData("2231")
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client.connect(ADDR)
        input("+++++++++++")

    def send_data(self, data, packageType: PackageType):
        protocol_socket_level.send_package(data, self.__client, packageType)
        print(f"[SEND_DATA] Client send to {SERVER}: {data}")

    def receive_data(self):
        data = protocol_socket_level.receive_package(self.__client)
        # TODO: להבין למה זה עושה מלא "None"
        if data is not None:
            self.__user_data.set_msg(data)
            print(f"[RECEIVE_DATA] Client receive from {SERVER}: {self.data}")
