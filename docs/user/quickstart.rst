.. _quickstart:

Quickstart:
===========

**import**::

        from ohmslaw import Ohms


**calculate resistance in ohms:**::

        >>> from ohmslaw import Ohms
        >>> 
        >>> o = Ohms()
        >>> results = o.resistance(48, 4)
        >>> 
        >>> print(results)
        12.0
        >>> 

**returns the electrical current:**::

        >>> from ohmslaw import Ohms
        >>> 
        >>> o = Ohms()
        >>> results = o.current(12, 4)
        >>> 
        >>> print(results)
        3.0
