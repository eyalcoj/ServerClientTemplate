import socket
from abc import ABC, abstractmethod
from enum import Enum


class Constance:
    HEADER = 5
    FORMAT = 'utf-8'
    PACKET_ID_LENGTH = 1


class PacketId(Enum):
    TEXT = 1
    IMG = 2


class PacketHandling(ABC):
    @staticmethod
    def crate_packet(packet_id: PacketId, data: str):
        return packet_id.value + data

    def brake_packet(self, data: str):
        packet_id = data[:Constance.PACKET_ID_LENGTH]
        pure_data = data[Constance.PACKET_ID_LENGTH:]
        if packet_id == PacketId.TEXT.value:
            self.__text_handling(pure_data)
        if packet_id == PacketId.TEXT.value:
            self.__img_handling(pure_data)

    @abstractmethod
    def __text_handling(self, data):
        pass

    @abstractmethod
    def __img_handling(self, data):
        pass


def send_package(data: str, conn: socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
    try:
        if data:
            data_length = len(data)
            encode_data_length = str(data_length).encode(Constance.FORMAT)
            encode_data_length = b' ' * (Constance.HEADER - len(encode_data_length)) + encode_data_length
            conn.send(encode_data_length + data.encode(Constance.FORMAT))

    except Exception as e:
        print(f"[ERROR] in send_package: {e}")


def receive_package(conn: socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
    try:
        organized_data_length = conn.recv(Constance.HEADER)
        if organized_data_length:
            organized_data_length = int(organized_data_length.decode(Constance.FORMAT))
            data = conn.recv(organized_data_length).decode(Constance.FORMAT)
            return data

    except Exception as e:
        if e is "[WinError 10054] An existing connection was forcibly closed by the remote host":
            return e
        else:
            print(f"[ERROR] in send_package: {e}")
