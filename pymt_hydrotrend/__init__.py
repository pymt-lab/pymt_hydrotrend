#! /usr/bin/env python

from .bmi import Hydrotrend

__all__ = ["Hydrotrend"]

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
