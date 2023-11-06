from src.servers.server_socket_level import Server_socket_level

DISCONNECT_MESSAGE = "!"


class Server_data_level(Server_socket_level):
    def handle_data(self):
        pass

    def is_connected(self, conn, addr):
        if self.data == DISCONNECT_MESSAGE:
            print(f"[DISCONNECT] {addr} disconnected.")
            conn.close()
            return False
        return True
