import socket
import threading

from src.data_base import ServerDataBase, CommunicationData
from src.protocols import protocol_socket_level
from src.protocols.protocol_socket_level import PackageType

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!"


class ServerSocketLevel:
    def __init__(self, server_data_base: ServerDataBase):
        self.server_data_base = server_data_base
        self.data = None
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind(ADDR)
        print("[STARTING] ServerSocketLevel is starting...")
        self.__start_connection()

    def __start_connection(self):
        self.__server.listen()
        print(f"[LISTENING] ServerSocketLevel is listening on {SERVER}")
        while True:
            conn, addr = self.__server.accept()
            communication_data = CommunicationData(conn, addr)
            self.server_data_base.add_server_user_data(communication_data)
            thread = threading.Thread(target=self.__handle_client, args=(communication_data, ))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

    def __handle_client(self, communication_data: CommunicationData):
        print(f"[NEW CONNECTION] {communication_data.get_addr()} connected.")
        connected = True
        while connected:
            self.receive_data(communication_data)
            connected = self.server_data_base.is_connected(communication_data)

    def receive_data(self, communication_data: CommunicationData):
        data = protocol_socket_level.receive_package(communication_data.get_conn())
        # TODO: להבין למה זה עושה מלא "None"
        if data is not None:
            self.data = data
            print(f"[RECEIVE_DATA] ServerSocketLevel receive from {communication_data.get_addr()}: {self.data}")

    @staticmethod
    def send_data(communication_data: CommunicationData, data, packageType: PackageType):
        protocol_socket_level.send_package(data, communication_data.get_conn(), packageType)
        print(f"[SEND_DATA] ServerSocketLevel send to {communication_data.get_addr()}: {data}")


