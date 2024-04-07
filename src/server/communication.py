import pickle
import socket
import sqlite3
import threading

from src.abstract_user_things import SingleConnection
from src.data_class import ConnectionData


class Constance:
    PORT = 5050
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    FORMAT = 'utf-8'
    DATABASE_FILE_LOCATION = r"'users_database.db'"


class ServerClientConnection(SingleConnection):

    def __init__(self, connection_data: ConnectionData):
        super().__init__(connection_data)

    def handle_data(self, packet_type, data):
        if packet_type == 1:
            print(f"[CLIENT] handle text: {data}")

        if packet_type == 2:
            print(f"CLIENT] handle pic")

class ServerDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS key_value_pairs
                                  (key TEXT PRIMARY KEY, value BLOB)''')
        self.conn.commit()

    def add(self, key=None, user_connection=None, age=None):
        try:
            key_str = str(key)
            data = pickle.dumps({"name": name, "age": age})
            self.cursor.execute('INSERT OR REPLACE INTO key_value_pairs VALUES (?, ?)', (key_str, data))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print(f"Key '{key}' already exists.")
            return False
        except Exception as e:
            print("Error adding data:", e)
            return False

    def remove(self, key):
        try:
            key_str = str(key)
            self.cursor.execute('DELETE FROM key_value_pairs WHERE key=?', (key_str,))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error removing data:", e)
            return False

    def update(self, key, name=None, age=None):
        try:
            key_str = str(key)
            new_dict = self.get(key_str) or {}
            if name:
                new_dict["name"] = name
            if age:
                new_dict["age"] = age

            data = pickle.dumps(new_dict)
            self.cursor.execute('INSERT OR REPLACE INTO key_value_pairs VALUES (?, ?)', (key_str, data))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error updating data:", e)
            return False

    def get(self, key):
        try:
            key_str = str(key)
            self.cursor.execute('SELECT value FROM key_value_pairs WHERE key=?', (key_str,))
            row = self.cursor.fetchone()
            if row:
                return pickle.loads(row[0])
            else:
                print(f"Key '{key}' not found.")
                return None
        except Exception as e:
            print("Error retrieving data:", e)
            return None


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
            server_client_connection = ServerClientConnection(connection_data)
            server_client_connection.open_connection()
            threading.Thread(target=self.menage_database_connection, args=(server_client_connection,))
            # self.__server_database.add(connection_data)

    def menage_database_connection(self, server_client_connection):
        while server_client_connection.is_alive():
            pass
        self.__server_database.remove(server_client_connection)

    def remove_user(self, server_client_connection):
        # TODO: need to check if this method works
        pass


    def remove_all_users(self):
        pass
