import socket
import threading
from abc import ABC, abstractmethod

from src.protocols import protocol_socket_level
from src.protocols.protocol_socket_level import PackageType

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!"


class Server_socket_level(ABC):
    def __init__(self):
        self.data = None
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind(ADDR)
        print("[STARTING] Server_socket_level is starting...")
        self.__start_connection()

    def __start_connection(self):
        self.__server.listen()
        print(f"[LISTENING] Server_socket_level is listening on {SERVER}")
        while True:
            conn, addr = self.__server.accept()
            thread = threading.Thread(target=self.__handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

    def __handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")
        connected = True
        while connected:
            self.receive_data(conn, addr)
            connected = self.is_connected(conn, addr)

    def receive_data(self, conn, addr):
        data = protocol_socket_level.receive_package(conn)
        # TODO: להבין למה זה עושה מלא "None"
        if data is not None:
            self.data = data
            print(f"[RECEIVE_DATA] Server_socket_level receive from {addr}: {self.data}")

    @staticmethod
    def send_data(conn, addr, data, packageType: PackageType):
        protocol_socket_level.send_package(data, conn, packageType)
        print(f"[SEND_DATA] Server_socket_level send to {addr}: {data}")

    @abstractmethod
    def handle_data(self):
        pass

    @abstractmethod
    def is_connected(self, conn, addr):
        pass
