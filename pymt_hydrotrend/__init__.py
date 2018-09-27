#! /usr/bin/env python

from .bmi import Hydrotrend

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
