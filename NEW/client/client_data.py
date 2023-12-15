import socket
import threading
from dataclasses import dataclass

from NEW import protocol
from NEW.protocol import PacketHandling, PacketId

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


class ClientData(PacketHandling):
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
            data = self.receive_data()
            self.__user_data.append(data)
            self.brake_packet(data)
        self.__connection_data.get_conn().close()
        print(f"[CONNECTION CLOSED] to server disconnected.")

    def send_data(self, data, packet_id: PacketId):
        protocol.send_package(self.crate_packet(packet_id, data), self.__connection_data.get_conn())
        print(f"[SEND_DATA] Client send to server: {packet_id, data}")

    def receive_data(self):
        data = protocol.receive_package(self.__connection_data.get_conn())
        if data is not None:
            print(f"[RECEIVE_DATA] Client receive from server: {data}")
            return data

    def disconnecting_from_server(self):
        # TODO: need to check if this method works
        self.__is_handle_connection = False

    def __text_handling(self, data):
        print(data)

    def __img_handling(self, data):
        print("save... \n download img")
