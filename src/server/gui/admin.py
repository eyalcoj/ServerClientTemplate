import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget

from src.server.gui.admin_user_data import AdminUserDataWindow


class AdminMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.usersQList = QListWidget()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Clickable Rows')
        self.layout = QVBoxLayout()

        self.usersQList.itemClicked.connect(self.on_item_clicked)
        self.add_row_button = QPushButton('Add Row')
        self.add_row_button.clicked.connect(lambda: self.add_list_item("shalom"))

        self.layout.addWidget(self.usersQList)
        self.layout.addWidget(self.add_row_button)

        self.setLayout(self.layout)

    def on_item_clicked(self, item):
        user_name = item.text()
        self.open_admin_user_data_window(user_name)

    def add_list_item(self, text):
        self.usersQList.addItem(text)

    def open_admin_user_data_window(self, user_name):
        # Pass reference to self (AdminMainWindow instance) when creating AdminUserDataWindow
        second_window = AdminUserDataWindow(user_name, self)
        second_window.show()

    def remove_selected_row(self):
        selected_item = self.usersQList.currentItem()
        if selected_item:
            self.usersQList.takeItem(self.usersQList.row(selected_item))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = AdminMainWindow()
#     ex.show()
#     sys.exit(app.exec_())
