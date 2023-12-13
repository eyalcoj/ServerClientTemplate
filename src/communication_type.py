from enum import Enum


class PacketType(Enum):
    LENGTH = 0
    DATA = 1


class DataType(Enum):
    TEXT = 0
    LOG_IN = 1
