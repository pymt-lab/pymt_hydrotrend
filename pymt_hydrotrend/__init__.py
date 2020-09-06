#! /usr/bin/env python
import pkg_resources

__version__ = pkg_resources.get_distribution("pymt_hydrotrend").version


from .bmi import Hydrotrend

__all__ = [
    "Hydrotrend",
]
