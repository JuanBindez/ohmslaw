.. _find_resistor:

Find Resistor
=============

**find the resistance value to limit the electrical voltage of a circuit:**::

        >>> o = Ohms()
        >>> results = o.find_resistor(source=48, 
        ...                           component_voltage=12,
        ...                           component_current=1)
        >>> 
        >>> print(results)
        36.0
        >>> 
