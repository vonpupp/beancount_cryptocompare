=======================
beancount-cryptocompare
=======================


.. image:: https://img.shields.io/pypi/v/beancount_cryptocompare.svg
        :target: https://pypi.python.org/pypi/beancount_cryptocompare

.. image:: https://img.shields.io/travis/vonpupp/beancount_cryptocompare.svg
        :target: https://travis-ci.org/vonpupp/beancount_cryptocompare

.. image:: https://readthedocs.org/projects/beancount-cryptocompare/badge/?version=latest
        :target: https://beancount-cryptocompare.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/vonpupp/beancount_cryptocompare/shield.svg
     :target: https://pyup.io/repos/github/vonpupp/beancount_cryptocompare/
     :alt: Updates


Beancount cryptocompare prices source


* Free software: GNU General Public License v3
* Documentation: https://beancount-cryptocompare.readthedocs.io.


How to install
--------------

Add the package to the `PYTHONPATH` variable on your shell

```
PYTHONPATH=$HOME/path/to/beancount_cryptocompare/beancount_cryptocompare
export PYTHONPATH
```


How to use
----------

You should be able to use it as follows:

```
bean-price -e USD:cryptocompareusd/ETH
```


Features
--------

* Cryptocompare prices query with automatic conversion to USD
* [In progress] Cryptocompare prices query with automatic conversion to EUR
* [In progress] Cryptocompare prices query with automatic conversion to BTC

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

