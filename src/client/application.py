import sys

from PyQt5.QtWidgets import QApplication

from src.client.communication import ClientServerConnection
from src.client.gui import MyGUI


class ClientApplication:
    def __init__(self):
        __communication = ClientServerConnection()
        app = QApplication(sys.argv)
        gui = MyGUI()
        gui.show()
        sys.exit(app.exec_())
