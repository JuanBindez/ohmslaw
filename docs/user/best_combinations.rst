.. _best_combinations:

Best Combinations
=================

**With this method you find the appropriate combination for your component:**::

        >>> from ohmslaw import Ohms
        >>> 
        >>> o = Ohms()
        >>> 
        >>> SOURCE_VOLTAGE = 48
        >>> COMPONENT_VOLTAGE = 3
        >>> COMPONENT_CURRENT = 0.02  # Corrente desejada para o componente (por exemplo, LED)
        >>> 
        >>> resistors = [200, 44, 350, 3, 1200, 500]
        >>> 
        >>> best_combination, resulting_voltage = o.best_combination(SOURCE_VOLTAGE, COMPONENT_VOLTAGE, COMPONENT_CURRENT, resistors)
        >>> 
        >>> print(f"Best combination of resistors: {best_combination}")
        Best combination of resistors: (200, 350, 1200, 500)
        >>> print(f"Resulting voltage on the component: {resulting_voltage:.2f}V")
        Resulting voltage on the component: 3.00V
        >>> 

