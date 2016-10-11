from wlm.reading_error import ReadingError

def test_reason_no_value():
    e = ReadingError(0)
    assert(e.reason == 'No value')

def test_reason_no_signal():
    e = ReadingError(-1)
    assert(e.reason == 'No signal')

def test_reason_bad_signal():
    e = ReadingError(-2)
    assert(e.reason == 'Bad signal')

def test_reason_low_signal():
    e = ReadingError(-3)
    assert(e.reason == 'Low signal')

def test_reason_big_signal():
    e = ReadingError(-4)
    assert(e.reason == 'Big signal')

def test_reason_missing():
    e = ReadingError(-5)
    assert(e.reason == 'Wavelength meter missing')

def test_reason_not_available():
    e = ReadingError(-6)
    assert(e.reason == 'Wavelength meter not available')

def test_no_pulse():
    e = ReadingError(-8)
    assert(e.reason == 'No pulse')

def test_unknown_error():
    e = ReadingError(100)
    assert(e.reason == 'Unknown')
