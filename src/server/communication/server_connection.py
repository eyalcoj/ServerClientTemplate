import socket

from src.data_class import ConnectionData
from src.server.db.users_db import UsersDatabase
from src.server.user import ServerUser


class Constance:
    PORT = 5050
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    FORMAT = 'utf-8'


class ServerConnection:

    def __init__(self, users_database: UsersDatabase):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind(Constance.ADDR)
        self.__run = True
        self.__users_database = users_database
        self.__counter = 0
        self.open_connection()

    def open_connection(self):
        self.__server.listen()

        print("[RUN] server is running.")
        while self.__run:
            conn, addr = self.__server.accept()
            connection_data = ConnectionData(conn, addr)
            server_user = ServerUser(connection_data)
            server_user.get_conn().open_connection()
            self.handle_connection(server_user)
            # threading.Thread(target=self.menage_database_connection, args=(server_client_connection,))

    # def menage_database_connection(self, server_client_connection):
    #     while server_client_connection.is_alive():
    #         pass
    def handle_connection(self, server_user: ServerUser):
        while server_user.get_data_base().get_user().get("name") is None:
            pass
        self.__users_database.add_user(server_user.get_data_base().get_user().get("name"), server_user)

    def remove_user(self, server_client_connection):
        # TODO: need to check if this method works
        pass

    def remove_all_users(self):
        pass
