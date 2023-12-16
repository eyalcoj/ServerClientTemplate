import socket
import threading

from src.data_class import ConnectionData
from src.user import User

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


class ServerConnection:
    def __init__(self):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind(ADDR)
        self.__users = []
        self.__run = True
        self.__start_connections()

    def __start_connections(self):
        self.__server.listen()
        print("[RUN] server is running.")
        while self.__run:
            conn, addr = self.__server.accept()
            connection_data = ConnectionData(conn, addr)
            server_user = User(connection_data)
            self.__users.append(server_user)
            thread = threading.Thread(target=server_user.handle_connection)
            thread.start()

    @staticmethod
    def disconnect_user(user: User):
        # TODO: need to check if this method works
        user.disconnect_user()
        del user

    def disconnect_server(self):
        # TODO: need to check if this method works
        for server_user in self.__users:
            self.disconnect_user(server_user)
        self.__run = False
