from enum import Enum

class ReadCommand(Enum):
    exhaustTemperature = bytes([0x04, 0x04, 0x14, 0x75])
    supplyTemperature = bytes([0x04, 0x04, 0x14, 0x73])
    extractTemperature = bytes([0x04, 0x04, 0x14, 0x74])
    outdoorTemperature = bytes([0x04, 0x04, 0x14, 0x72])
    roomTemperature = bytes([0x01, 0x04, 0x03, 0x00])
    roomTemperatureCalculated = bytes([0x00, 0x04, 0x14, 0x96])
    humidity = bytes([0x01, 0x04, 0x14, 0x70])
    bypass = bytes([0x00, 0x04, 0x14, 0x60])
    filterPercent = bytes([0x01, 0x04, 0x14, 0x6a])
    boost = bytes([0x01, 0x04, 0x15, 0x30])
    supply_fan_speed = bytes([0x00, 0x04, 0x14, 0x50])
    exhaust_fan_speed = bytes([0x00, 0x04, 0x14, 0x51])
    fan_step = bytes([0x01, 0x04, 0x15, 0x61])
    away_mode = bytes([0x01, 0x04, 0x15, 0x22])
    battery_percent = bytes([0x01, 0x04, 0x03, 0x0f])
    automatic_bypass = bytes([0x01, 0x04, 0x17, 0x06])
    operation_mode = bytes([0x01, 0x04, 0x14, 0x12])

class UpdateCommand(Enum):
    boost_activate = bytes([0x01, 0x06, 0x14, 0x60, 0x01])
    boost_deactivate = bytes([0x01, 0x06, 0x14, 0x63, 0x00])
    bypass_activate = bytes([0x00, 0x06, 0x14, 0x60, 0x01])
    bypass_deactivate = bytes([0x00, 0x06, 0x14, 0x60, 0x00])
    automatic_bypass_deactivate = bytes([0x01, 0x06, 0x17, 0x06, 0x01])
    automatic_bypass_activate = bytes([0x01, 0x06, 0x17, 0x06, 0x00])
    operation_mode_demand = bytes([0x01, 0x06, 0x14, 0x12, 0x00])
    operation_mode_program = bytes([0x01, 0x06, 0x14, 0x12, 0x01])
    operation_mode_manual = bytes([0x01, 0x06, 0x14, 0x12, 0x02])
    set_fan_step_1 = bytes([0x01, 0x06, 0x15, 0x61, 0x01])
    set_fan_step_2 = bytes([0x01, 0x06, 0x15, 0x61, 0x02])
    set_fan_step_3 = bytes([0x01, 0x06, 0x15, 0x61, 0x03])
    set_fan_step_4 = bytes([0x01, 0x06, 0x15, 0x61, 0x04])
    set_fan_step_5 = bytes([0x01, 0x06, 0x15, 0x61, 0x05])
    set_fan_step_6 = bytes([0x01, 0x06, 0x15, 0x61, 0x06])
    set_fan_step_7 = bytes([0x01, 0x06, 0x15, 0x61, 0x07])
    set_fan_step_8 = bytes([0x01, 0x06, 0x15, 0x61, 0x08])
    set_fan_step_9 = bytes([0x01, 0x06, 0x15, 0x61, 0x09])
    set_fan_step_10 = bytes([0x01, 0x06, 0x15, 0x61, 0xA])
