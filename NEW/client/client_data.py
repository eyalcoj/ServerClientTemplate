import socket
import threading

from NEW import protocol

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


class ClientData:
    def __init__(self):
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__start_connection()

    def __start_connection(self):
        print(f"[CONNECT] client ({self.__client}) connecting to the server")
        self.__client.connect(ADDR)
        thread = threading.Thread(target=self.__handle_server, args=(self.__client,))
        thread.start()
        self.send_data("hi server")

    def __handle_server(self, addr):
        print(f"[HANDEL_SERVER] {addr} handel server.")
        connected = True
        while connected:
            self.receive_data()

    def send_data(self, data):
        protocol.send_package(data, self.__client)
        print(f"[SEND_DATA] Client send to {SERVER}: {data}")

    def receive_data(self):
        data = protocol.receive_package(self.__client)
        if data is not None:
            print(f"[RECEIVE_DATA] Client receive from {SERVER}: {data}")


if __name__ == "__main__":
    server_data = ClientData()
