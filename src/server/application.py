import sys
import threading

from PyQt5.QtWidgets import QApplication

from src.server.communication import ServerConnection
from src.server.gui.admin import AdminMainWindow


class ServerApplication:
    def __init__(self):
        threading.Thread(target=self.crate_communication)
        app = QApplication(sys.argv)
        ex = AdminMainWindow()
        ex.show()
        sys.exit(app.exec_())

    @staticmethod
    def crate_communication():
        __communication = ServerConnection()
