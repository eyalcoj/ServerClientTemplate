import socket
from enum import Enum


class Constance:
    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!"


def send_package(data, conn: socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
    if data:
        encoded_organized_data = data.encode(Constance.FORMAT)
        encoded_organized_data_length = len(encoded_organized_data)
        send_length = str(encoded_organized_data_length).encode(Constance.FORMAT)
        send_length += b' ' * (Constance.HEADER - len(send_length))
        conn.send(send_length)
        conn.send(encoded_organized_data)


def receive_package(conn):
    organized_data_length = conn.recv(Constance.HEADER)
    if organized_data_length:
        organized_data_length = int(organized_data_length.decode(Constance.FORMAT))
        conn.recv(organized_data_length).decode(Constance.FORMAT)


