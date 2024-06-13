.. _find_resistor:

Find Resistor:
==============

**find the resistance value to limit the electrical voltage of a circuit:**::

        >>> from ohmslaw import Ohms
        >>> 
        >>> o = Ohms()
        >>> results = o.find_resistor(source=48, component_voltage=12)# Led
        >>> 
        >>> print(results)
        1800.0
        >>> 
