import socket
from abc import ABC, abstractmethod
from enum import Enum


class Constants:
    HEADER = 5
    FORMAT = 'utf-8'
    PACKET_ID_LENGTH = 1


class PacketType(Enum):
    TEXT = 1
    IMG = 2


def __send_by_socket(payload: str, conn: socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
    try:
        if payload:
            payload_length = len(payload)
            encode_payload_length = str(payload_length).encode(Constants.FORMAT)
            encode_payload_length = b' ' * (Constants.HEADER - len(encode_payload_length)) + encode_payload_length
            conn.send(encode_payload_length + payload.encode(Constants.FORMAT))

    except Exception as e:
        print(f"[ERROR] in send_package: {e}")


def __receive_by_socket(conn: socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
    try:
        organized_payload_length = conn.recv(Constants.HEADER)
        if organized_payload_length:
            organized_payload_length = int(organized_payload_length.decode(Constants.FORMAT))
            payload = conn.recv(organized_payload_length).decode(Constants.FORMAT)
            return payload

    except Exception as e:
        if e is "[WinError 10054] An existing connection was forcibly closed by the remote host":
            return e
        else:
            print(f"[ERROR] in send_package: {e}")


def __wrap_packet(packet_type: PacketType, payload: str):  # why is payload string and not bytes?
    return packet_type.value + payload


def __extract_packet(payload: str):
    packet_type = payload[:Constants.PACKET_ID_LENGTH]
    data = payload[Constants.PACKET_ID_LENGTH:]
    return packet_type, data


def send(packet_type: PacketType, payload: str, conn: socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
    __send_by_socket(__wrap_packet(packet_type, payload), conn)


def recv(conn: socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
    return __extract_packet(__receive_by_socket(conn))

