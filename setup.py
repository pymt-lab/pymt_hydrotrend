#! /usr/bin/env python
import os
import sys

import numpy as np
import versioneer
from setuptools import find_packages, setup

from distutils.extension import Extension


import numpy as np


include_dirs = [np.get_include(), os.path.join(sys.prefix, "include")]


libraries = ["bmi_hydrotrend"]


library_dirs = []
if sys.platform.startswith("win"):
    library_dirs.append(os.path.join(sys.prefix, "Library", "lib"))


define_macros = []

undef_macros = []


extra_compile_args = []


ext_modules = [
    Extension(
        "pymt_hydrotrend.lib._bmi",
        ["pymt_hydrotrend/lib/_bmi.pyx"],
        language="c",
        include_dirs=include_dirs,
        libraries=libraries,
        library_dirs=library_dirs,
        define_macros=define_macros,
        undef_macros=undef_macros,
        extra_compile_args=extra_compile_args,
    )
]

packages = find_packages()
entry_points = {
    "pymt.plugins": [
        "Hydrotrend=pymt_hydrotrend.bmi:Hydrotrend",
    ]
}

cmdclass = versioneer.get_cmdclass()

setup(
    name="pymt_hydrotrend",
    author="Eric Hutton",
    description="PyMT plugin hydrotrend",
    version=versioneer.get_version(),
    setup_requires=["cython"],
    ext_modules=ext_modules,
    packages=packages,
    cmdclass=cmdclass,
    entry_points=entry_points,
    include_package_data=True,
)
