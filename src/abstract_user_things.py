import threading
from abc import ABC, abstractmethod

from src import protocol
from src.data_class import ConnectionData
from src.protocol import PacketType


class SingleConnection(ABC):
    def __init__(self, connection_data: ConnectionData):
        self.connection_data = connection_data
        self.__is_handle_connection = False

    def handle_connection(self):
        self.__is_handle_connection = True
        print(f"[NEW CONNECTION] {self.connection_data.get_addr()} connected.")
        while self.__is_handle_connection:
            packet_type, data = self.receive_data()
            self.handle_data(packet_type, data)
        self.connection_data.get_conn().close()
        print(f"[CONNECTION CLOSED] {self.connection_data.get_addr()} disconnected.")

    def receive_data(self):
        packet_type, data = protocol.recv2(self.connection_data.get_conn())
        print(f"[RECEIVE_DATA] receive from {self.connection_data.get_addr()}: {data}")
        return packet_type, data

    def send_data(self, packet_type: PacketType, data):
        protocol.send2(packet_type, data, self.connection_data.get_conn())
        print(f"[SEND_DATA] send to {self.connection_data.get_addr()}: {data}")

    def close_connection(self):
        # TODO: need to check if this method works
        self.__is_handle_connection = False

    def open_connection(self):
        handle_server_thread = threading.Thread(target=self.handle_connection)
        handle_server_thread.start()

    @staticmethod
    @abstractmethod
    def handle_data(packet_type, data):
        pass
