from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from .commands import ReadCommand
from .commands import UpdateCommand

class DanfossClient:
    def __init__(self, host):
        self._host = host

    def command(self, command):
        if isinstance(command, ReadCommand):
            return self._read_command(command)

        if isinstance(command, UpdateCommand):
            return self._update_command(command)

        raise Exception("Not yet implemented")

    def read_all(self):
        result = {}

        for command in ReadCommand:
            result[command] = self.command(command)

        return result

    def _update_command(self, command):
        if command in {UpdateCommand.boost_activate, UpdateCommand.boost_deactivate}:
            self._update_switch(command)

            return self._read_bit(ReadCommand.boost)

        raise Exception("Unknown comand: {0}".format(command))

    def _update_switch(self, command):
        self._read_value(command)

    def _read_command(self, command):
        if(command == ReadCommand.exhaustTemperature or
           command == ReadCommand.outdoorTemperature or
           command == ReadCommand.extractTemperature or
           command == ReadCommand.supplyTemperature):
            return self._read_temperature(command)

        if(command == ReadCommand.humidity or
           command == ReadCommand.filterPercent
                ):
            return self._read_percent(command)

        if(command == ReadCommand.bypass or
           command == ReadCommand.boost
                ):
            return self._read_bit(command)

        if(command == ReadCommand.supply_fan_speed or
           command == ReadCommand.exhaust_fan_speed
                ):
            return self._read_short(command)

        if(command == ReadCommand.fan_step):
            return self._read_byte(command)

        raise Exception("Unknown command: {0}".format(command))

    def _read_temperature(self, command):
        return self._read_short(command)/100

    def _read_bit(self, command):
        result = self._read_value(command)
        return result[0] != 0x00

    def _read_percent(self, command):
        result = self._read_value(command)
        return int(result[0]) * 100/255

    def _read_value(self, command):
        with socket(AF_INET, SOCK_STREAM) as s:
            s.connect((self._host, 30046))
            s.send(command.value)
            result = s.recv(63)
            s.close()
            
            return result

    def _read_byte(self, command):
        result = self._read_value(command)
        
        r = bytes([result[0]])
        
        return int.from_bytes(r, byteorder = 'big', signed=True)

    def _read_short(self, command):
        result = self._read_value(command)
        
        r = bytes([result[0], result[1]])
        
        return int.from_bytes(r, byteorder = 'big', signed=True)
