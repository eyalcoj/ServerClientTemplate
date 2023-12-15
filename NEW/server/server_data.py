import socket
import threading
from dataclasses import dataclass

from NEW import protocol
from NEW.protocol import PacketHandling, PacketId

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


@dataclass
class ConnectionData:
    __conn: socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    __addr: str

    def get_conn(self):
        return self.__conn

    def get_addr(self):
        return self.__addr


class ServerUser(PacketHandling):
    def __init__(self, connection_data: ConnectionData):
        self.__connection_data = connection_data
        self.__is_handle_connection = False
        self.__user_data = []

    def handle_client(self):
        self.__is_handle_connection = True
        print(f"[NEW CONNECTION] {self.__connection_data.get_addr()} connected.")
        while self.__is_handle_connection:
            data = self.receive_data()
            self.__user_data.append(data)
            self.brake_packet(data)
        self.__connection_data.get_conn().close()
        print(f"[CONNECTION CLOSED] {self.__connection_data.get_addr()} disconnected.")

    def receive_data(self):
        data = protocol.receive_package(self.__connection_data.get_conn())
        if data is not None:
            print(f"[RECEIVE_DATA] Server_socket_level receive from {self.__connection_data.get_addr()}: {data}")
            return data

    def send_data(self, connection_data_of_addressee: ConnectionData, packet_id: PacketId, data):
        protocol.send_package(self.crate_packet(packet_id, data), connection_data_of_addressee.get_conn())
        print(f"[SEND_DATA] Server_socket_level send to {connection_data_of_addressee.get_addr()}: {data}")

    def get_is_handle_connection(self):
        return self.__is_handle_connection

    def disconnect_user(self):
        # TODO: need to check if this method works
        self.__is_handle_connection = False

    def __text_handling(self, data):
        print(data)

    def __img_handling(self, data):
        print("save... \n download img")


class ServerData:
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
            server_user = ServerUser(connection_data)
            thread = threading.Thread(target=server_user.handle_client)
            thread.start()
            while not server_user.get_is_handle_connection():
                pass
            self.__users.append(server_user)

    @staticmethod
    def disconnect_user(server_user: ServerUser):
        # TODO: need to check if this method works
        server_user.disconnect_user()
        del server_user

    def disconnect_server(self):
        # TODO: need to check if this method works
        for server_user in self.__users:
            self.disconnect_user(server_user)
        self.__run = False
