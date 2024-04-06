import socket
import pickle

from src.abstract_user_things import SingleConnection
from src.data_class import ConnectionData


class Constance:
    PORT = 5050
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    FORMAT = 'utf-8'
    DATABASE_FILE_LOCATION = r"src/server/db.txt"


class ServerConnection:

    def __init__(self):
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind(Constance.ADDR)
        self.__server_database = ServerDatabase(Constance.DATABASE_FILE_LOCATION)
        self.__run = True
        self.open_connection()

    def open_connection(self):
        self.__server.listen()
        print("[RUN] server is running.")
        while self.__run:
            conn, addr = self.__server.accept()
            connection_data = ConnectionData(conn, addr)
            basic_connection = UserConnection(connection_data)
            basic_connection.open_connection()
            self.__server_database.add_data(connection_data, basic_connection=basic_connection)

    def remove_user(self, connection_data):
        # TODO: need to check if this method works
        pass

    def remove_all_users(self):
        pass


class UserConnection(SingleConnection):

    def __init__(self, connection_data: ConnectionData):
        super().__init__(connection_data)

    @staticmethod
    def handle_data(packet_type, data):
        if packet_type == 1:
            print(f"[CLIENT] handle text: {data}")

        if packet_type == 2:
            print(f"CLIENT] handle pic")


class ServerDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.database = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.database, file)

    def add_data(self, key, basic_connection=None, age=None, email=None):
        key = f"{key}"
        if key in self.database:
            print(f"Key '{key}' already exists. Use update_data method to modify existing data.")
            return False
        else:
            self.database[key] = {"basic_connection": basic_connection, "age": age, "email": email}
            self.save_data()  # Save data to file after adding
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
            self.save_data()  # Save data to file after updating
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
            self.save_data()  # Save data to file after deletion
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
