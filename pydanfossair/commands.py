from enum import Enum

class ReadCommand(Enum):
    exhaustTemperature = bytes([0x04, 0x04, 0x14, 0x75])
    SupplyTemperature = 2
    ExtractTemperature = 3
    OutdoorTemperature = 4
    Hummidity = 5
    Bypass = 6
    Boost = 7

class UpdateCommand(Enum):
    BypassActivate = 1
    BypassDeactivate = 2

