from abc import ABC, abstractmethod

from src import protocol
from src.data_class import ConnectionData
from src.protocol import PacketType


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


class User(PacketHandler):
    def __init__(self, connection_data: ConnectionData):
        self.__connection_data = connection_data
        self.__is_handle_connection = False
        self.__user_data = []

    def handle_client(self):
        self.__is_handle_connection = True
        print(f"[NEW CONNECTION] {self.__connection_data.get_addr()} connected.")
        while self.__is_handle_connection:
            packet_type, data = self.receive_data()
            self.__user_data.append((packet_type, data))
            self.handle_data(packet_type, data)
        self.__connection_data.get_conn().close()
        print(f"[CONNECTION CLOSED] {self.__connection_data.get_addr()} disconnected.")

    def receive_data(self):
        packet_type, data = protocol.recv(self.__connection_data.get_conn())
        if data is not None:
            print(f"[RECEIVE_DATA] Server_socket_level receive from {self.__connection_data.get_addr()}: {data}")
            return packet_type, data

    def send_data(self, packet_type: PacketType, data):
        protocol.send(packet_type, data, self.__connection_data.get_conn())
        print(f"[SEND_DATA] Server_socket_level send to {self.__connection_data.get_addr()}: {data}")

    def get_is_handle_connection(self):
        return self.__is_handle_connection

    def disconnect_user(self):
        # TODO: need to check if this method works
        self.__is_handle_connection = False

    def __text_handling(self, data):
        print(data)

    def __img_handling(self, data):
        print("save... \n download img")
