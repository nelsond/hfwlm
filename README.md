# pySIS [![Build Status](https://travis-ci.org/nelsond/hfwlm.svg?branch=master)](https://travis-ci.org/nelsond/hfwlm)

Library for controlling HighFinesse wavelength meters.

## Install

Install with pip

```shell
$ pip install git+git://github.com/nelsond/hfwlm.git
```

## Example usage

```python
from wlm import WavelengthMeter

wm = WavelengthMeter()
wm.channel_count # => 8

# set switcher channel
wm.switcher_channel = 1

wm.switch_mode # => False

# enable switch mode
wm.switch_mode = True

# read properties of channels
channel = wm.channels[0]
channel.use # => False
channel.use = True
channel.show = True
channel.frequency # => 359.212...
```

## Development

Install requirements for development environment

```shell
$ pip install -r requirements/dev.txt
```

Run tests

```shell
$ py.test tests/
```

Generate coverage report

```shell
$ py.test --cov=wlm tests/
```
