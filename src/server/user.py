from src.data_class import ConnectionData
from src.server.communication.server_client_connection import ServerClientConnection
from src.server.db.user_data import ServerUserDatabase
from src.server.gui.admin_user_data import AdminUserDataWindow


class ServerUser:
    def __init__(self, connection_data: ConnectionData):
        self.__data_base = ServerUserDatabase()
        self.__conn = ServerClientConnection(connection_data, self.__data_base)
        self.__gui = AdminUserDataWindow(self.__conn, self.__data_base)

    def get_conn(self):
        return self.__conn

    def get_gui(self):
        return self.__gui

    def get_data_base(self):
        return self.__data_base
