from wlm.wavelength_meter import WavelengthMeter
from wlm.channel import Channel
import wlm.helper
from support import MockDLL
import pytest
from random import randint

@pytest.fixture
def mock_dll():
    return MockDLL(0)

@pytest.fixture
def channel_count():
    return randint(1, 8)

# .__init__
def test_init(mock_dll):
    wlm = WavelengthMeter(mock_dll)
    assert(wlm.dll == mock_dll)

# ._initChannels
def test_initChannels_creates_correct_number_of_channels(channel_count):
    mock_dll = MockDLL(channel_count)
    wlm = WavelengthMeter(mock_dll)
    assert(len(wlm.channels) == channel_count)

def test_initChannels_creates_channels(channel_count):
    mock_dll = MockDLL(channel_count)
    wlm = WavelengthMeter(mock_dll)
    assert(type(wlm.channels[0]) == Channel)

# .channel_count (property)
def test_channel_count_returns_number_of_channels():
    mock_dll = MockDLL(8)
    wlm = WavelengthMeter(mock_dll)
    assert(wlm.channel_count == 8)

# .switcher_channel (property)
def test_switcher_channel_returns_active_channel():
    mock_dll = MockDLL(1)
    wlm = WavelengthMeter(mock_dll)
    assert(wlm.switcher_channel == 1)

def test_switcher_channel_sets_active_channel():
    mock_dll = MockDLL(1)
    wlm = WavelengthMeter(mock_dll)
    wlm.switcher_channel = 2
    assert(wlm.switcher_channel == 2)

def test_switcher_channel_sets_active_channel_from_channel_object():
    mock_dll = MockDLL(1)
    wlm = WavelengthMeter(mock_dll)
    channel = Channel(2, wlm=wlm)
    wlm.switcher_channel = channel
    assert(wlm.switcher_channel == 2)

# .switch_mode (property)
def test_switch_mode_returns_switch_status_when_on():
    mock_dll = MockDLL(1)
    wlm = WavelengthMeter(mock_dll)
    assert(wlm.switch_mode == True)

def test_switch_mode_returns_switch_status_when_off():
    mock_dll = MockDLL(0)
    wlm = WavelengthMeter(mock_dll)
    assert(wlm.switch_mode == False)

def test_switch_mode_turns_switch_on():
    mock_dll = MockDLL(0)
    wlm = WavelengthMeter(mock_dll)
    wlm.switch_mode = True
    assert(mock_dll._value == 1)

def test_switch_mode_turns_switch_off():
    mock_dll = MockDLL(1)
    wlm = WavelengthMeter(mock_dll)
    wlm.switch_mode = False
    assert(mock_dll._value == 0)
