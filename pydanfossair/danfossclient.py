from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from .commands import ReadCommand
from .commands import UpdateCommand
from struct import *
class DanfossClient:
    def __init__(self, config):
        self._host = config["host"]
#        self._socket = socket(AF_INET, SOCK_STREAM)

    def command(self, command):
        if isinstance(command, ReadCommand):
            return self._readCommand(command)
        else:
            raise Exception("Not yet implemented")

    def _readCommand(self, command):
        if(command == ReadCommand.exhaustTemperature or
           command == ReadCommand.outdoorTemperature or
           command == ReadCommand.extractTemperature or
           command == ReadCommand.supplyTemperature):
            return self._readTemperature(command)

        if(command == ReadCommand.humidity or
           command == ReadCommand.filterPercent
                ):
            return self._readPercent(command)

        if(command == ReadCommand.bypass
                ):
            return self._readBit(command)

        raise Exception("Unknown command")

    def _readTemperature(self, command):
        return self._readShort(command)/100

    def _readBit(self, command):
        result = self._readValue(command)
        return result[0] != 0x00

    def _readPercent(self, command):
        result = self._readValue(command)
        return int(result[0]) * 100/255

    def _readValue(self, command):
        with socket(AF_INET, SOCK_STREAM) as s:
            s.connect((self._host, 30046))
            s.send(command.value)
            result = s.recv(63)
            s.close()

            return result

    def _readShort(self, command):
       result = self._readValue(command)

       r = bytes([result[0], result[1]])
       return int.from_bytes(r, byteorder = 'big', signed=True)
