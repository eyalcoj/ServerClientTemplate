from clients.client_data_level import ClientDataLevel
from clients.client_socket_level import ClientSocketLevel


class MainClient:
    def __init__(self):
        client_socket_level = ClientSocketLevel()
        client_data_level = ClientDataLevel("hi")


if __name__ == "__main__":
    MainClient()
