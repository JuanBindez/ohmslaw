.. _parallel:

Parallel
========

**To return resistor value in parallel, simply pass the resistors as an argument in the parallel method:**::

        >>> from ohmslaw import Ohms
        >>> 
        >>> R1, R2, R3 = 280, 450, 100
        >>> 
        >>> o = Ohms()
        >>> parallel = o.parallel(R1, R2, R3)
        >>> 
        >>> print("Resistor in parallel = ", parallel)
        Resistors in parallel =  63.31658291457286
        >>> 
