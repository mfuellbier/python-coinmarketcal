#!/usr/bin/env python
import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.dirname(__file__)

exec(open(os.path.join(here, 'coinmarketcal', 'version.py')).read())
setup(name = "coinmarketcal",
    version = version_string, #@UndefinedVariable,
    description = "Python wrapper for coinmarketcal.com",
    author = "mfuellbier",
    maintainer_email = "gregoryberzin@gmail.com",
    license = "BSD",
    url = "https://github.com/trikota/python-coinmarketcal",
    packages = [
        'coinmarketcal',
    ],
    install_requires = ["requests"],
    platforms = ["POSIX", "Windows"],
    use_2to3 = False,
    zip_safe = False,
    long_description = open(os.path.join(here, "README.md"), "r").read(),
)


