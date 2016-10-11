from .helper import wlm_dll
from .channel import Channel

class WavelengthMeter(object):
    def __init__(self, dll_path=r'C:\\Windows\System32\wlmdata.dll'):
        if type(dll_path) == str:
            self.dll = wlm_dll(dll_path)
        else:
            self.dll = dll_path

        self._initChannels()

    def _initChannels(self):
        self.channels = []
        for num in range(1, self.channel_count + 1):
            channel = Channel(num, wlm=self)
            self.channels.append(channel)

    @property
    def channel_count(self):
        return self.dll.GetChannelsCount(0)

    @property
    def switcher_channel(self):
        return self.dll.GetSwitcherChannel(0)

    @switcher_channel.setter
    def switcher_channel(self, channel):
        if type(channel) == Channel:
            channel = channel.num

        self.dll.SetSwitcherChannel(channel)

    @property
    def switch_mode(self):
        return self.dll.GetSwitcherMode(0) == 1

    @switch_mode.setter
    def switch_mode(self, mode):
        mode = 1 if mode else 0
        self.dll.SetSwitcherMode(mode)
