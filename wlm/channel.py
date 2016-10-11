from ctypes import byref, c_long
from .reading_error import ReadingError

class Channel(object):
    def __init__(self, num, wlm):
        self.num = num
        self._wlm = wlm

    def switch(self):
        self._wlm.switcher_channel = self.num

    @property
    def frequency(self):
        value = self._dll.GetFrequencyNum(self.num, 0)

        if value > 0:
            return value
        else:
            raise ReadingError(value)

    @property
    def wavelength(self):
        value = self._dll.GetWavelengthNum(self.num, 0)

        if value > 0:
            return value
        else:
            raise ReadingError(value)

    @property
    def state(self):
        use, show = c_long(), c_long()
        self._dll.GetSwitcherSignalStates(self.num, byref(use), byref(show))
        return { 'use': use.value == 1, 'show': show.value == 1 }

    @state.setter
    def state(self, state):
        use = 1 if state.get('use', self.state['use']) else 0
        show = 1 if state.get('show', self.state['show']) else 0
        self._dll.SetSwitcherSignalStates(self.num, use, show)

    @property
    def use(self):
        return self.state['use']

    @use.setter
    def use(self, enable):
        self.state = { 'use': enable }

    @property
    def show(self):
        return self.state['show']

    @show.setter
    def show(self, enable):
        self.state = { 'show': enable }

    @property
    def _dll(self):
        return self._wlm.dll
