import socket
from enum import Enum


class Constance:
    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!"


class PackageType(Enum):
    TEXT = 0
    IMAGE = 1


def send_package(data, conn: socket.socket(socket.AF_INET, socket.SOCK_STREAM), package_type: PackageType):
    if data:
        organized_data = f"{package_type.value}{data}"
        encoded_organized_data = organized_data.encode(Constance.FORMAT)
        encoded_organized_data_length = len(encoded_organized_data)
        send_length = str(encoded_organized_data_length).encode(Constance.FORMAT)
        send_length += b' ' * (Constance.HEADER - len(send_length))
        conn.send(send_length)
        conn.send(encoded_organized_data)


def receive_package(conn):
    organized_data_length = conn.recv(Constance.HEADER)
    if organized_data_length:
        organized_data_length = int(organized_data_length.decode(Constance.FORMAT))
        return handle_organized_data(conn.recv(organized_data_length).decode(Constance.FORMAT))


def handle_organized_data(organized_data):
    if int(organized_data[:1]) == PackageType.TEXT.value:
        return organized_data[1:]

    if int(organized_data[:1]) == PackageType.IMAGE.value:
        pass
