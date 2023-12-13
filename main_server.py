from src.data_base import ServerDataBase
from src.servers.server_data_level import ServerDataLevel
from src.servers.server_socket_level import ServerSocketLevel


class MainServer:
    def __init__(self):
        server_data_base = ServerDataBase()
        server_socket_level = ServerSocketLevel(server_data_base)
        server_data_level = ServerDataLevel(server_data_base, server_socket_level)


if __name__ == "__main__":
    MainServer()
