import socket


class Constance:
    HEADER = 5
    FORMAT = 'utf-8'


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

