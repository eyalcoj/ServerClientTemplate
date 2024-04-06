import socket
import threading

from src.abstract_user_things import SingleConnection
from src.data_class import ConnectionData


class Constance:
    PORT = 5050
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)


class ClientConnection(SingleConnection):
    def __init__(self):
        __client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(ConnectionData(__client, Constance.ADDR))
        super().__init__(ConnectionData(__client, Constance.ADDR))
        self.connection_data.get_conn().connect(self.connection_data.get_addr())
        self.open_connection()

    @staticmethod
    def handle_data(packet_type, data):
        if packet_type == 1:
            print(f"[CLIENT] handle text: {data}")

        if packet_type == 2:
            print(f"CLIENT] handle pic")
