from socket import socket

class DanfossClient:
    def __init__(self, config):
        self._socket = socket(socket.AF_INET, socket.SOCKET_STREAM)

    def command(self, command):
        if isinstance(command, CommandRead):
            return self._readCommand(command)
        else:
            raise Exception("Not yet implemented")

    def _readCommand(self, command):
        if command == ReadCommand.exhaustTemperature:
            return self._readShort(command)

        raise Exception("Unknown command")

    def _readShort(self, command):
        with socket(socket.AF_INET, socket.SOCKET_STREAM) as s:
            s.connect(("10.100.0.11", 30046))
            s.send(bytes([0x04, 0x04, 0x14, 0x75]))

            result = s.recv(63)
            s.close()
            r = bytes([result[0], result[1]])

            return int.from_bytes(r, byteorder = 'big')/100

