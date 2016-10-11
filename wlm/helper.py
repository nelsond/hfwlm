from ctypes import c_long, c_double, POINTER

def wlm_dll(path):
    from ctypes import WinDLL
    dll = WinDLL(path)

    dll.GetChannelsCount.restype   = c_long
    dll.GetChannelsCount.argtypes  = [c_long]

    dll.GetSwitcherChannel.restype  = c_long
    dll.GetSwitcherChannel.argtypes = [c_long]

    dll.SetSwitcherChannel.restype  = c_long
    dll.SetSwitcherChannel.argtypes = [c_long]

    dll.GetSwitcherMode.restype  = c_long
    dll.GetSwitcherMode.argtypes = [c_long]

    dll.SetSwitcherMode.restype  = c_long
    dll.SetSwitcherMode.argtypes = [c_long]

    dll.GetSwitcherSignalStates.restype = c_long
    dll.GetSwitcherSignalStates.argtypes = [c_long, POINTER(c_long), POINTER(c_long)]

    dll.SetSwitcherSignalStates.restype = c_long
    dll.SetSwitcherSignalStates.argtypes = [c_long, c_long, c_long]

    dll.GetFrequencyNum.restype  = c_double
    dll.GetFrequencyNum.argtypes = [c_long, c_double]

    dll.GetWavelengthNum.restype  = c_double
    dll.GetWavelengthNum.argtypes = [c_long, c_double]

    return dll
