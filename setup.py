# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

here = os.path.dirname(os.path.abspath(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

with open(os.path.join(here, 'requirements' , 'common.txt')) as f:
    required = f.read().splitlines()

setup(
    name='hfwlm',

    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    description='Library for controlling HighFinesse wavelength meters.',
    long_description=long_description,

    url='https://github.com/nelsond/hfwlm',

    author='Nelson Darkwah Oppong',
    author_email='n@darkwahoppong.com',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Stable',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='highfiness wavelength meter',

    packages=['wlm'],

    install_requires=required
)
