from wlm.channel import Channel
from wlm.reading_error import ReadingError
import pytest
from random import randint, random
from support import MockDLL

class MockWavelengthMeter(object):
    def __init__(self, value=None):
        self._value = value
        self.dll = MockDLL(value)

@pytest.fixture
def wlm():
    return MockWavelengthMeter()

# .__init__
def test_init_sets_channel_number(wlm):
    channel = Channel(1, wlm=wlm)
    assert(channel.num == 1)

def test_init_sets_wlm_parent(wlm):
    channel = Channel(1, wlm=wlm)
    assert(channel._wlm == wlm)

# .switch
def test_switch_changes_channel(wlm):
    num = randint(1, 8)
    channel = Channel(num, wlm=wlm)
    channel.switch()

    assert(channel._wlm.switcher_channel == num)

# .frequency (property)
def test_frequency_returns_value():
    value = random() * 1e12 * 700e2
    wlm = MockWavelengthMeter(value)
    channel = Channel(randint(1, 8), wlm=wlm)

    assert(channel.frequency == value)

def test_frequency_raises_for_invalid_value():
    value = 0
    wlm = MockWavelengthMeter(value)
    channel = Channel(randint(1, 8), wlm=wlm)

    with pytest.raises(ReadingError) as e:
        channel.frequency
        assert(e.reason)

# .wavelength (property)
def test_get_wavelength_returns_value():
    value = random() * 1e12 * 700e2
    wlm = MockWavelengthMeter(value)
    channel = Channel(randint(1, 8), wlm=wlm)

    assert(channel.wavelength == value)

def test_wavelength_raises_for_invalid_value():
    value = 0
    wlm = MockWavelengthMeter(value)
    channel = Channel(randint(1, 8), wlm=wlm)

    with pytest.raises(ReadingError) as e:
        channel.wavelength
        assert(e.reason)

# .state (property)
def test_state_returns_signal_state(wlm):
    channel = Channel(randint(1, 8), wlm=wlm)
    assert(channel.state == { 'use': False, 'show': False })

def test_state_sets_signal_state(wlm):
    channel = Channel(randint(1, 8), wlm=wlm)
    channel.state = { 'use': True, 'show': False }

# .use (property)
def test_use_returns_use_state(wlm):
    channel = Channel(randint(1, 8), wlm=wlm)
    assert(channel.use == False)

def test_use_sets_use_state(wlm):
    channel = Channel(randint(1, 8), wlm=wlm)
    channel.use = True

# .show (property)
def test_show_returns_show_state(wlm):
    channel = Channel(randint(1, 8), wlm=wlm)
    assert(channel.show == False)

def test_show_sets_show_state(wlm):
    channel = Channel(randint(1, 8), wlm=wlm)
    channel.show = True
