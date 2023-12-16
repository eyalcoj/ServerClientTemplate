from dataclasses import dataclass
import socket


@dataclass
class ConnectionData:
    __conn: socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    __addr: tuple[str, int]

    def get_conn(self):
        return self.__conn

    def get_addr(self):
        return self.__addr
