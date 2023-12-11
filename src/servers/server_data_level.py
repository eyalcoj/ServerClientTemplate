from src.data_base import ServerDataBase
from src.servers.server_socket_level import ServerSocketLevel

DISCONNECT_MESSAGE = "!"


class ServerDataLevel:
    def __init__(self, server_data_base: ServerDataBase, server_socket_level: ServerSocketLevel):
        self.server_data_base = server_data_base
        self.server_socket_level = server_socket_level
