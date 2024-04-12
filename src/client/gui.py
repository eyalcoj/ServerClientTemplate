import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

from src.client.communication import ClientServerConnection
from src.client.user_data import ClientUserData


class MyGUI(QWidget):
    def __init__(self, conn: ClientServerConnection, user_data: ClientUserData):
        super().__init__()
        self.__conn = conn
        self.__user_data = user_data
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Indicator GUI')
        self.setGeometry(100, 100, 400, 300)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Create three rows
        for _ in range(3):
            row_layout = QHBoxLayout()
            main_layout.addLayout(row_layout)

            # Indicator text
            indicator_label = QLabel()
            indicator_label.setFixedSize(20, 20)
            indicator_label.setStyleSheet("background-color: red; border-radius: 10px;")
            row_layout.addWidget(indicator_label)

            # Spot with text
            spot_label = QLabel('Some Text')
            row_layout.addWidget(spot_label)

            # Button
            button = QPushButton('Toggle')
            button.clicked.connect(lambda checked, label=indicator_label: self.toggle_indicator(label))
            row_layout.addWidget(button)

        # Additional button
        additional_button = QPushButton('Additional Button')
        main_layout.addWidget(additional_button)

    def toggle_indicator(self, label):
        # Toggle indicator color
        if label.styleSheet() == "background-color: red; border-radius: 10px;":
            label.setStyleSheet("background-color: green; border-radius: 10px;")
        else:
            label.setStyleSheet("background-color: red; border-radius: 10px;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MyGUI()
    gui.show()
    sys.exit(app.exec_())
