import sys
import threading

from PyQt5.QtWidgets import QApplication

from src.client.communication import ClientServerConnection
from src.client.gui import MyGUI
from src.client.user_data import ClientUserData


class Client:
    # def __init__(self):
    #     self.__conn = None
    #     self.__users_database = UsersDatabase()
    #     self.__crate_communication_thread = threading.Thread(target=self.crate_communication)
    #     self.__crate_communication_thread.start()
    #     app = QApplication(sys.argv)
    #     assert self.__conn is None, "check the server"
    #     self.__gui = AdminMainWindow(self.__conn, self.__users_database)
    #     self.__gui.show()
    #     sys.exit(app.exec_())
    #
    # def crate_communication(self):
    #     self.__conn = ServerConnection(self.__users_database)

    def __init__(self):
        self.__conn = None
        self.__user_data = ClientUserData()
        self.__crate_communication_thread = threading.Thread(target=self.crate_communication)
        self.__crate_communication_thread.start()
        app = QApplication(sys.argv)
        while self.__conn is None:
            pass
        self.__gui = MyGUI(self.__conn, self.__user_data)
        self.__gui.show()
        sys.exit(app.exec_())

    def crate_communication(self):
        self.__conn = ClientServerConnection(self.__user_data)
