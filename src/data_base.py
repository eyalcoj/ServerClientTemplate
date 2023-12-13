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
    __user_name: str
    __communication_data: CommunicationData
    __data: str

    def __init__(self, communication_data: CommunicationData):
        self.__communication_data = communication_data

    def set_user_name(self, user_name):
        self.__user_name = user_name

    def get_user_name(self):
        return self.__user_name

    def get_communication_data(self):
        return self.__communication_data

    def set_data(self, data: str):
        self.__data = data


@dataclass
class ServerDataBase:
    __list: list

    def __init__(self):
        self.__list = []

    def add_server_user_data(self, communication_data: CommunicationData):
        self.__list.append(ServerUserData(communication_data))

    def set_user_name(self, communication_data: CommunicationData, user_name: str):
        for server_user_data in self.__list:
            if server_user_data.get_communication_data() == communication_data:
                server_user_data.set_user_name(user_name)

    def is_connected(self, communication_data: CommunicationData):
        for server_user_data in self.__list:
            if server_user_data.get_communication_data() == communication_data:
                return True
        return False

    def set_data(self, communication_data: CommunicationData, data):
        for server_user_data in self.__list:
            if server_user_data.get_communication_data() == communication_data:
                server_user_data.set_data(data)

# @dataclass
# class UserData:
#     __user_id: str
#     __user_data: str
#
#     def __init__(self, user_name: str):
#         self.__user_id = user_name
#
#     def set_data(self, data: str):
#         self.__user_data = data
