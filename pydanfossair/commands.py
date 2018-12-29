from enum import Enum

class ReadCommand(Enum):
    ExhaustTemperature = 1
    SupplyTemperature = 2
    ExtractTemperature = 3
    OutdoorTemperature = 4
    Hummidity = 5
    Bypass = 6
    Boost = 7

class UpdateCommand(Enum):
    BypassActivate = 1
    BypassDeactivate = 2

