from __future__ import absolute_import

from pymt.framework.bmi_bridge import bmi_factory

from .bmi import Hydrotrend

Hydrotrend = bmi_factory(Hydrotrend)

del bmi_factory
