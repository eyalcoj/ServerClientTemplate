import threading
from abc import ABC, abstractmethod

from src import protocol
from src.data_class import ConnectionData
from src.protocol import PacketType


class SingleConnection(ABC):
    def __init__(self, connection_data: ConnectionData):
        self.__handle_server_thread = None
        self.connection_data = connection_data
        self.__is_handle_connection = False

    def handle_connection(self):
        self.__is_handle_connection = True
        print(f"[NEW CONNECTION] {self.connection_data.get_addr()} connected.")
        while self.__is_handle_connection:
            print("shalom")
            packet_type, data = self.receive_data()
            if packet_type != PacketType.ERROR:
                print("shalom", packet_type, data)
                self.handle_data(packet_type, data)
        self.connection_data.get_conn().close()
        print(f"[CONNECTION CLOSED] {self.connection_data.get_addr()} disconnected.")

    def receive_data(self):
        packet_type, data = protocol.recv2(self.connection_data.get_conn())
        if packet_type != PacketType.ERROR:
            print(f"[RECEIVE_DATA] receive from {self.connection_data.get_addr()}: {data}")
        return packet_type, data

    def send_data(self, packet_type: PacketType, data):
        protocol.send2(packet_type, data, self.connection_data.get_conn())
        print(f"[SEND_DATA] send to {self.connection_data.get_addr()}: {data}")

    def close_connection(self):
        self.send_data(PacketType.DISCONNECT, "")
        self.clean_disconnect()

    def open_connection(self):
        self.__handle_server_thread = threading.Thread(target=self.handle_connection)
        self.__handle_server_thread.start()

    def clean_disconnect(self):
        self.__is_handle_connection = False
        self.__handle_server_thread.join()

    def is_alive(self):
        return self.__is_handle_connection and self.__handle_server_thread.is_alive()

    @abstractmethod
    def handle_data(self, packet_type, data):
        if PacketType(packet_type) == PacketType.DISCONNECT:
            self.clean_disconnect()

