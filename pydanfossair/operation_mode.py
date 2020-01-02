from enum import Enum

class OperationMode(Enum):
    demand = bytes([0x00])
    program = bytes([0x01])
    manual = bytes([0x02])
