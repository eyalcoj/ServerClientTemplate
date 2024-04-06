import socket
import threading

from src.abstract_user_things import BasicConnection
from src.data_class import ConnectionData


class Constance:
    PORT = 5050
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)


class ClientConnection(BasicConnection):
    def __init__(self):
        super().__init__(ConnectionData(self.__server, Constance.ADDR))

    def close_connection(self):
        super(ClientConnection, self).close_connection()

    def open_connection(self):
        self.__connection_data.get_conn().connect(self.__connection_data.get_addr())
        print("[RUN] client is running.")
        handle_server_thread = threading.Thread(target=self.handle_connection)
        handle_server_thread.start()

    @staticmethod
    def handle_data(packet_type, data):
        if packet_type == 1:
            print(f"[CLIENT] handle text: {data}")

        if packet_type == 2:
            print(f"CLIENT] handle pic")
