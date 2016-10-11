class MockDLL(object):
    def __init__(self, value=0):
        self._value = value

    def GetChannelsCount(self, _):
        return self._value

    def GetFrequencyNum(self, num, _):
        return self._value

    def GetSwitcherChannel(self, _):
        return self._value

    def GetSwitcherMode(self, _):
        return self._value

    def GetSwitcherSignalStates(self, num, use, show):
        return 0

    def GetWavelengthNum(self, num, _):
        return self._value

    def SetSwitcherChannel(self, channel):
        self._value = channel

    def SetSwitcherMode(self, mode):
        self._value = mode

    def SetSwitcherSignalStates(self, num, use, show):
        return 0
