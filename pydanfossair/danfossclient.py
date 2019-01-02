from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from .commands import ReadCommand
from .commands import UpdateCommand

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

        raise Exception("Unknown command")

    def _readTemperature(self, command):
        return self._readShort(command)/100

    def _readShort(self, command):
        with socket(AF_INET, SOCK_STREAM) as s:
            s.connect((self._host, 30046))
            s.send(command.value)
            result = s.recv(63)
            s.close()
            r = bytes([result[0], result[1]])

            return int.from_bytes(r, byteorder = 'big')

