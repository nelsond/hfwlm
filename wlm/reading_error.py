class ReadingError(Exception):
    def __init__(self, value):
        self._value = round(value)
        super(ReadingError, self).__init__(self.reason)

    @property
    def reason(self):
        if self._value == 0:
            return 'No value'
        if self._value == -1:
            return 'No signal'
        elif self._value == -2:
            return 'Bad signal'
        elif self._value == -3:
            return 'Low signal'
        elif self._value == -4:
            return 'Big signal'
        elif self._value == -5:
            return 'Wavelength meter missing'
        elif self._value == -6:
            return 'Wavelength meter not available'
        elif self._value == -8:
            return 'No pulse'

        return 'Unknown'
