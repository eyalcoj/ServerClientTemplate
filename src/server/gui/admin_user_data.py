from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

from src.server.communication.server_client_connection import ServerClientConnection
from src.server.user import ServerUserDatabase


class AdminUserDataWindow(QWidget):
    def __init__(self, conn: ServerClientConnection, data_base: ServerUserDatabase):
        super().__init__()
        self.__dict = data_base
        self.user_name = data_base.get_user().get("name")
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.user_name)
        self.setGeometry(100, 100, 400, 200)

        main_layout = QVBoxLayout(self)

        for _ in range(2):
            row_layout = QHBoxLayout()
            main_layout.addLayout(row_layout)

            indicator_label = QLabel()
            indicator_label.setFixedSize(20, 20)
            indicator_label.setStyleSheet("background-color: red; border-radius: 10px;")
            row_layout.addWidget(indicator_label)

            button = QPushButton('Toggle')
            button.clicked.connect(lambda checked, label=indicator_label: self.toggle_indicator(label))
            row_layout.addWidget(button)

        additional_button = QPushButton('Remove Row')
        additional_button.clicked.connect(self.remove_row)
        main_layout.addWidget(additional_button)

    def toggle_indicator(self, label):
        if label.styleSheet() == "background-color: red; border-radius: 10px;":
            label.setStyleSheet("background-color: green; border-radius: 10px;")
        else:
            label.setStyleSheet("background-color: red; border-radius: 10px;")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     gui = AdminUserDataWindow("User Name", None, None)  # Pass None for the main_window argument for testing
#     gui.show()
#     sys.exit(app.exec_())
