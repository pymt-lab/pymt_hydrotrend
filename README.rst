==========
hydrotrend
==========


.. image:: https://img.shields.io/pypi/v/pymt_hydrotrend.svg
        :target: https://pypi.python.org/pypi/pymt_hydrotrend

.. image:: https://img.shields.io/travis/mcflugen/pymt_hydrotrend.svg
        :target: https://travis-ci.org/mcflugen/pymt_hydrotrend

.. image:: https://readthedocs.org/projects/pymt_hydrotrend/badge/?version=latest
        :target: https://pymt_hydrotrend.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


PyMT plugin for hydrotrend


* Free software: MIT license
* Documentation: https://hydrotrend.readthedocs.io.


---------------
Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3.6
  conda activate pymt

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

.. code::

  conda install pymt

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt --channel conda-forge

--------------------------
Installing pymt_hydrotrend
--------------------------

Once `pymt` is installed, the dependencies of `pymt_hydrotrend` can
be installed with:

.. code::

  conda install hydrotrend

Until `pymt_hydrotrend` is available on `conda-forge`, it must
by installed from source,

.. code::

  git clone https://github.com/mcflugen/pymt_hydrotrend
  cd pymt_hydrotrend
  python setup.py install
