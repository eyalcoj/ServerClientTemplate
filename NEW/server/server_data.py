import socket
import threading

from NEW import protocol

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!"


class ServerData:
    def __init__(self):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind(ADDR)
        print("[STARTING] Server_socket_level is starting...")
        self.__start_connection()

    def __start_connection(self):
        self.__server.listen()
        print(f"[LISTENING] Server_socket_level is listening on {SERVER}")
        while True:
            conn, addr = self.__server.accept()
            thread = threading.Thread(target=self.__handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
            self.send_data(conn, addr, "hi client")

    def __handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")
        connected = True
        while connected:
            self.receive_data(conn, addr)

    def receive_data(self, conn, addr):
        data = protocol.receive_package(conn)
        # TODO: להבין למה זה עושה מלא "None"
        if data is not None:
            print(f"[RECEIVE_DATA] Server_socket_level receive from {addr}: {data}")

    @staticmethod
    def send_data(conn, addr, data):
        protocol.send_package(data, conn)
        print(f"[SEND_DATA] Server_socket_level send to {addr}: {data}")


if __name__ == "__main__":
    server_data = ServerData()
