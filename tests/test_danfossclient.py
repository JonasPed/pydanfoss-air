"""Unit tests for DanfossClient read decoding.

A FakeSocket returns a canned 63-byte frame per register so the decoding logic
can be exercised without hardware. The response byte(s) mirror what the CCM
returns on the wire; values are taken from a live Danfoss Air CCM.
"""
import pytest

from pydanfossair.commands import ReadCommand
from pydanfossair.danfossclient import DanfossClient


class FakeSocket:
    """Minimal socket stand-in: echoes a per-register canned response frame."""

    def __init__(self, responses: dict[bytes, bytes]) -> None:
        self._responses = responses
        self._last = None

    def send(self, payload: bytes) -> int:
        self._last = payload
        return len(payload)

    def recv(self, _bufsize: int) -> bytes:
        # Frames are 63 bytes on the wire; only the leading data bytes matter.
        return self._responses[self._last].ljust(63, b"\x00")


def frame(*data: int) -> bytes:
    return bytes(data)


def client_with(register: ReadCommand, *data: int) -> tuple[DanfossClient, FakeSocket]:
    sock = FakeSocket({register.value: frame(*data)})
    return DanfossClient("test"), sock


@pytest.mark.parametrize(
    ("raw", "expected"),
    [(100, 100), (44, 44), (0, 0)],
    ids=["fresh-100", "depleted-44", "empty-0"],
)
def test_battery_is_raw_percent_not_rescaled(raw: int, expected: int) -> None:
    """Battery is a plain 0-100 byte, not a 0-255 value to rescale by 100/255."""
    client, sock = client_with(ReadCommand.battery_percent, raw)
    assert client._read_command(ReadCommand.battery_percent, sock) == expected


def test_fan_speed_percent_is_raw_byte() -> None:
    """New airflow-percentage register returns the raw 0-100 byte."""
    client, sock = client_with(ReadCommand.fan_speed_percent, 54)
    assert client._read_command(ReadCommand.fan_speed_percent, sock) == 54


@pytest.mark.parametrize("step", [1, 3, 5, 10])
def test_fan_step_is_raw_step_not_times_ten(step: int) -> None:
    """fan_step is the stored manual step (1-10), no longer multiplied by 10."""
    client, sock = client_with(ReadCommand.fan_step, step)
    assert client._read_command(ReadCommand.fan_step, sock) == step


def test_humidity_still_rescaled() -> None:
    """Humidity remains a 0-255 value rescaled to a percentage (unchanged)."""
    client, sock = client_with(ReadCommand.humidity, 145)
    assert client._read_command(ReadCommand.humidity, sock) == pytest.approx(145 * 100 / 255)


def test_filter_percent_still_rescaled() -> None:
    """filterPercent remains a 0-255 value rescaled to a percentage (unchanged)."""
    client, sock = client_with(ReadCommand.filterPercent, 94)
    assert client._read_command(ReadCommand.filterPercent, sock) == pytest.approx(94 * 100 / 255)


def test_temperature_is_centidegrees() -> None:
    """Temperatures are a signed short in centidegrees (unchanged)."""
    client, sock = client_with(ReadCommand.roomTemperature, 0x09, 0x51)  # 2385 -> 23.85
    assert client._read_command(ReadCommand.roomTemperature, sock) == pytest.approx(23.85)


@pytest.mark.parametrize(
    ("raw", "expected"),
    [(0xFF, True), (0x01, True), (0x00, False)],
    ids=["on-ff", "on-01", "off-00"],
)
def test_bypass_is_true_when_nonzero(raw: int, expected: bool) -> None:
    """The 'on' state is any non-zero byte (firmware returns 0xff, not 0x01)."""
    client, sock = client_with(ReadCommand.bypass, raw)
    assert client._read_command(ReadCommand.bypass, sock) is expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [(0x00, True), (0x01, False)],
    ids=["auto-on", "auto-off"],
)
def test_automatic_bypass_is_inverted(raw: int, expected: bool) -> None:
    """automatic_bypass reads inverted relative to the raw bit."""
    client, sock = client_with(ReadCommand.automatic_bypass, raw)
    assert client._read_command(ReadCommand.automatic_bypass, sock) is expected
