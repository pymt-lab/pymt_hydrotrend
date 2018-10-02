==========
hydrotrend
==========


.. image:: https://img.shields.io/pypi/v/hydrotrend.svg
        :target: https://pypi.python.org/pypi/hydrotrend

.. image:: https://img.shields.io/travis/mcflugen/hydrotrend.svg
        :target: https://travis-ci.org/mcflugen/hydrotrend

.. image:: https://readthedocs.org/projects/hydrotrend/badge/?version=latest
        :target: https://hydrotrend.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


PyMT plugin for hydrotrend


* Free software: MIT license
* Documentation: https://hydrotrend.readthedocs.io.


Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

```
conda config --add channels conda-forge
```

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

```
conda install pymt
```

It is possible to list all of the versions of `pymt` available on your platform with:

```
conda search pymt --channel conda-forge
```

Installing pymt_hydrotrend
--------------------------

Once `pymt` is installed, the dependencies of `pymt_hydrotrend` can
be installed with:

```
conda install hydrotrend
```

Until `pymt_hydrotrend` is available on `conda-forge`, it must
by installed from source,

```
git clone https://github.com/mcflugen/pymt_hydrotrend
cd pymt_hydrotrend
python setup.py install
```