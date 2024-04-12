import sys
import threading

from PyQt5.QtWidgets import QApplication

from src.server.db.users_db import UsersDatabase
from src.server.communication.server_connection import ServerConnection
from src.server.gui.admin import AdminMainWindow


class Server:
    def __init__(self):
        self.__conn = None
        self.__users_database = UsersDatabase()
        self.__crate_communication_thread = threading.Thread(target=self.crate_communication)
        self.__crate_communication_thread.start()
        app = QApplication(sys.argv)
        assert self.__conn is None, "check the server"
        self.__gui = AdminMainWindow(self.__conn, self.__users_database)
        self.__gui.show()
        print("in her")
        sys.exit(app.exec_())

    def crate_communication(self):
        print("crate_communication befor")
        self.__conn = ServerConnection(self.__users_database)
        print("crate_communication after")