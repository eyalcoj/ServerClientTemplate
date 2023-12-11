from dataclasses import dataclass
from socket import socket


@dataclass
class CommunicationData:
    __conn: socket
    __addr: str

    def get_conn(self):
        return self.__conn

    def get_addr(self):
        return self.__addr


@dataclass
class ServerUserData:
    __user_id: str
    __communication_data: CommunicationData

    def __init__(self, communication_data: CommunicationData):
        self.__communication_data = communication_data

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_user_name(self):
        return self.__user_id

    def get_communication_data(self):
        return self.__communication_data


@dataclass
class ServerDataBase:

    __list: list

    def __init__(self):
        self.__list = []

    def add_server_user_data(self, communication_data: CommunicationData):
        self.__list.append(ServerUserData(communication_data))

    def get_communication(self, user_id: str):
        for server_user_data in self.__list:
            if server_user_data.get_user_name() == user_id:
                return server_user_data.get_communication_data()

    def connect_user_id(self, communication_data: CommunicationData, user_id: str):
        for server_user_data in self.__list:
            if server_user_data.get_communication_data() == communication_data:
                server_user_data.set_user_id(user_id)

    def is_connected(self, communication_data: CommunicationData):
        for server_user_data in self.__list:
            if server_user_data.get_communication_data() == communication_data:
                return True
        return False

