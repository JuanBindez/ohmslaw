.. _quickstart:

Quickstart:
===========

**import**::

        from ohmslaw import Ohms


**calculate resistance in ohms:**::

        >>> from ohmslaw import Ohms
        >>> 
        >>> o = Ohms()
        >>> results = o.resistance(V=48, I=4)
        >>> 
        >>> print(results)
        12.0
        >>> 

**returns the electrical current:**::

        >>> from ohmslaw import Ohms
        >>> 
        >>> o = Ohms()
        >>> results = o.current(V=12, R=4)
        >>> 
        >>> print(results)
        3.0
