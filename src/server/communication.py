import socket

from src.abstract_user_things import BasicConnection
from src.data_class import ConnectionData


class Constance:
    PORT = 5050
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    FORMAT = 'utf-8'


class ServerConnection(BasicConnection):

    def __init__(self):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind(Constance.ADDR)
        super().__init__(ConnectionData(self.__server, Constance.ADDR))
        self.__server_database = ServerDatabase()
        self.__run = True
        self.open_connection()

    def open_connection(self):
        self.__server.listen()
        print("[RUN] server is running.")
        while self.__run:
            conn, addr = self.__server.accept()
            connection_data = ConnectionData(conn, addr)
            self.__server_database.add_data(connection_data)

    def close_connection(self):
        # TODO: need to check if this method works
        self.__run = False
        super().close_connection()

    @staticmethod
    def handle_data(packet_type, data):
        if packet_type == 1:
            print(f"[CLIENT] handle text: {data}")

        if packet_type == 2:
            print(f"CLIENT] handle pic")

    def remove_user(self, connection_data):
        # TODO: need to check if this method works
        pass

    def remove_all_users(self):
        pass


class ServerDatabase:
    def __init__(self):
        self.database = {}

    def add_data(self, key, name=None, age=None, email=None):
        if key in self.database:
            print(f"Key '{key}' already exists. Use update_data method to modify existing data.")
            return False
        else:
            self.database[key] = {"name": name, "age": age, "email": email}
            print(f"Data added successfully for key '{key}'.")
            return True

    def update_data(self, key, name=None, age=None, email=None):
        if key in self.database:
            if name is not None:
                self.database[key]["name"] = name
            if age is not None:
                self.database[key]["age"] = age
            if email is not None:
                self.database[key]["email"] = email
            print(f"Data updated successfully for key '{key}'.")
            return True
        else:
            print(f"Key '{key}' does not exist. Use add_data method to add new data.")
            return False

    def get_data(self, key):
        return self.database.get(key, None)

    def delete_data(self, key):
        if key in self.database:
            del self.database[key]
            print(f"Data deleted successfully for key '{key}'.")
            return True
        else:
            print(f"Key '{key}' does not exist.")
            return False

    def display_all_data(self):
        if self.database:
            print("Database Contents:")
            for key, value in self.database.items():
                print(f"Key: {key}, Value: {value}")
        else:
            print("Database is empty.")
