import socket
import threading
from abc import ABC, abstractmethod
from dataclasses import dataclass

from src import protocol
from src.protocol import PacketType

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


@dataclass
class ConnectionData:
    __conn: socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    __addr: tuple

    def get_conn(self):
        return self.__conn

    def get_addr(self):
        return self.__addr


class PacketHandler(ABC):
    def handle_data(self, packet_type: PacketType, data: str):
        if packet_type == PacketType.TEXT.value:
            self.__text_handling(data)
        if packet_type == PacketType.IMG.value:
            self.__img_handling(data)

    @abstractmethod
    def __text_handling(self, payload):
        pass

    @abstractmethod
    def __img_handling(self, payload):
        pass


class ClientData(PacketHandler):
    def __init__(self):
        self.__connection_data = ConnectionData(socket.socket(socket.AF_INET, socket.SOCK_STREAM), ADDR)
        self.__is_handle_connection = False
        self.__user_data = []
        self.__connect_to_server()

    def __connect_to_server(self):
        self.__connection_data.get_conn().connect(self.__connection_data.get_addr())
        print("[RUN] client is running.")
        handle_server_thread = threading.Thread(target=self.__handle_server)
        handle_server_thread.start()

    def __handle_server(self):
        __is_handle_connection = True
        print(f"[NEW CONNECTION] to server conncted.")
        while __is_handle_connection:
            packet_type, data = self.receive_data()
            self.__user_data.append((packet_type, data))
            self.handle_data(packet_type, data)
        self.__connection_data.get_conn().close()
        print(f"[CONNECTION CLOSED] to server disconnected.")

    def send_data(self, data: str, packet_type: PacketType):
        protocol.send(packet_type, data, self.__connection_data.get_conn())
        print(f"[SEND_DATA] Client send to server: {packet_type, data}")

    def receive_data(self):
        packet_type, data = protocol.recv(self.__connection_data.get_conn())
        if data is not None:
            print(f"[RECEIVE_DATA] Client receive from server: {data}")
            return packet_type, data

    def disconnecting_from_server(self):
        # TODO: need to check if this method works
        self.__is_handle_connection = False

    def __text_handling(self, data):
        print(data)

    def __img_handling(self, data):
        print("save... \n download img")
