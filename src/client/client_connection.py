import socket
import threading

from src.data_class import ConnectionData
from src.user import User

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


class ClientConnection(User):
    def __init__(self):
        super().__init__(ConnectionData(socket.socket(socket.AF_INET, socket.SOCK_STREAM), ADDR))
        self.__is_handle_connection = False
        self.__user_data = []
        self.__connect_to_server()

    def __connect_to_server(self):
        self.__connection_data.get_conn().connect(self.__connection_data.get_addr())
        print("[RUN] client is running.")
        handle_server_thread = threading.Thread(target=self.__handle_server)
        handle_server_thread.start()

    def __handle_server(self):
        self.__is_handle_connection = True
        print(f"[NEW CONNECTION] connected to server.")
        while self.__is_handle_connection:
            packet_type, data = self.receive_data()
            self.__user_data.append((packet_type, data))
            self.handle_data(packet_type, data)
        self.__connection_data.get_conn().close()
        print(f"[CONNECTION CLOSED] to server disconnected.")

    def disconnecting_from_server(self):
        # TODO: need to check if this method works
        self.__is_handle_connection = False
