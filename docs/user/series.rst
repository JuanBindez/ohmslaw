.. _series:

Series
======

**you can calculate the resistors in series, passing the values ​​in the series() method:**::

        >>> from ohmslaw import Ohms
        >>> 
        >>> R1, R2, R3 = 280, 450, 100
        >>> 
        >>> o = Ohms()
        >>> series = o.series(R1, R2, R3)
        >>> 
        >>> print("Resistors in series = ", series)
        Resistors in series =  830
        >>> 
