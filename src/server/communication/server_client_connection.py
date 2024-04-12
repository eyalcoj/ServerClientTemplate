from src.abstract_user_things import SingleConnection
from src.data_class import ConnectionData
from src.protocol import PacketType
from src.server.db.user_data import ServerUserData


class ServerClientConnection(SingleConnection):

    def __init__(self, connection_data: ConnectionData, data_dict: ServerUserData):
        self.__data_dict = data_dict
        super().__init__(connection_data)

    def handle_data(self, packet_type, data):
        super(ServerClientConnection, self).handle_data(packet_type, data)
        if PacketType(packet_type) == PacketType.LOGIN:
            self.__data_dict.update_user(name=data, is_run_mouse=True, is_run_keyboard=True)
