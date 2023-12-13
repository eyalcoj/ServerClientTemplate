from socket import socket

from src.data_base import ServerDataBase, CommunicationData
from src.servers.server_socket_level import ServerSocketLevel
from src.communication_type import DataType

DISCONNECT_MESSAGE = "!"


class ServerDataLevel:
    def __init__(self, server_data_base: ServerDataBase, server_socket_level: ServerSocketLevel):
        self.server_data_base = server_data_base
        self.server_socket_level = server_socket_level

    def handle_data(self):
        server_data_base
        if len(data) is not 0:
            pure_data = data[0][1]
            communication_data = data[0][0]
            self.__data_type_action(communication_data, pure_data)

    def __data_type_action(self, communication_data: CommunicationData, data: str):
        if data[0] == DataType.TEXT.value:
            self.__text_coping(data[1:])
        if data[0] == DataType.LOG_IN.value:
            self.__log_in_coping(communication_data, data[1:])

    @staticmethod
    def __text_coping(data: str):
        print("[TEXT_COPING]")
        print(data)

    def __log_in_coping(self, communication_data: CommunicationData, data: str):
        print("[TEXT_LOGIN]")
        self.server_socket_level.login(data, communication_data)
