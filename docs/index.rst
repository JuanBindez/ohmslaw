.. ohmslaw documentation master file,

ohmslaw
============
Release v\ |version|. (:ref:`Installation<install>`)


.. image:: https://img.shields.io/pypi/v/ohmslaw.svg
  :alt: Pypi
  :target: https://pypi.python.org/pypi/ohmslaw/

.. image:: https://img.shields.io/pypi/pyversions/ohmslaw.svg
  :alt: Python Versions
  :target: https://pypi.python.org/pypi/ohmslaw/


**ohmslaw** ohmslaw is an open source tool written in Python designed for Ohmslaw calculate..
-------------------------------------------------------------------------------------------------------------------------------------------

**calculate resistance in ohms:**::

        >>> from ohmslaw import Ohms
        >>> 
        >>> o = Ohms()
        >>> results = o.resistance(48, 4)
        >>> 
        >>> print(results)
        12.0
        >>> 

Features
--------

- calculate Ohms
- Volts
- Current
- Resistance
- Watts

The User Guide
---------------
This part of the documentation begins with some background information about
the project, then focuses on step-by-step instructions for getting the most out
of ohmslaw.

.. toctree::
   :maxdepth: 2

   user/install
   user/cli
   user/volts
   user/current
   user/resistance
   user/watts
   user/find_resistor
   user/parallel
   user/series
   user/combinations
   user/best_combinations


The API Documentation
-----------------------------

If you are looking for information on a specific function, class, or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   api

