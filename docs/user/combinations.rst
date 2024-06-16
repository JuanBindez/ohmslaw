.. _combinations:

Combinations of Resistors
=========================

**This code allows you to experiment with different combinations of resistors and observe how the voltage across the LED changes, helping you find the most suitable combination to achieve the desired 3V. :**::

        >>> from ohmslaw import Ohms
        >>> 
        >>> LED_VOLTAGE = 3
        >>> SOURCE_VOLTAGE = 48
        >>> 
        >>> resistors = [200, 44, 350, 3, 1200, 500]
        >>> 
        >>> o = Ohms()
        >>> 
        >>> def calculate_voltage(selected_resistors):
        ...     total_resistance = o.series(*selected_resistors)
        ...     total_current = o.current(SOURCE_VOLTAGE, total_resistance)
        ...     led_voltage = total_current * LED_VOLTAGE
        ...     return led_voltage
        ... 
        >>> # Testing different combinations of resistors
        >>> for i in range(len(resistors)):
        ...     for j in range(i, len(resistors)):
        ...         combination = resistors[:i] + resistors[j:]
        ...         voltage = calculate_voltage(combination)
        ...         print(f"Resistors: {combination}, Voltage across LED: {voltage:.2f}V")
        ... 
        >>> # Checking the closest combination for 3V across the LED
        >>> best_combination = None
        >>> smallest_difference = float('inf')
        >>> 
        >>> for i in range(len(resistors)):
        ...     for j in range(i, len(resistors)):
        ...         combination = resistors[:i] + resistors[j:]
        ...         voltage = calculate_voltage(combination)
        ...         difference = abs(voltage - LED_VOLTAGE)
        ...         if difference < smallest_difference:
        ...             smallest_difference = difference
        ...             best_combination = combination
        ... 
        >>> print(f"Best combination of resistors: {best_combination} with voltage across LED: {calculate_voltage(best_combination):.2f}V")
        Resistors: [200, 44, 350, 3, 1200, 500], Voltage across LED: 0.06V
        Resistors: [44, 350, 3, 1200, 500], Voltage across LED: 0.07V
        Resistors: [350, 3, 1200, 500], Voltage across LED: 0.07V
        Resistors: [3, 1200, 500], Voltage across LED: 0.08V
        Resistors: [1200, 500], Voltage across LED: 0.08V
        Resistors: [500], Voltage across LED: 0.29V
        Resistors: [200, 44, 350, 3, 1200, 500], Voltage across LED: 0.06V
        Resistors: [200, 350, 3, 1200, 500], Voltage across LED: 0.06V
        Resistors: [200, 3, 1200, 500], Voltage across LED: 0.08V
        Resistors: [200, 1200, 500], Voltage across LED: 0.08V
        Resistors: [200, 500], Voltage across LED: 0.21V
        Resistors: [200, 44, 350, 3, 1200, 500], Voltage across LED: 0.06V
        Resistors: [200, 44, 3, 1200, 500], Voltage across LED: 0.07V
        Resistors: [200, 44, 1200, 500], Voltage across LED: 0.07V
        Resistors: [200, 44, 500], Voltage across LED: 0.19V
        Resistors: [200, 44, 350, 3, 1200, 500], Voltage across LED: 0.06V
        Resistors: [200, 44, 350, 1200, 500], Voltage across LED: 0.06V
        Resistors: [200, 44, 350, 500], Voltage across LED: 0.13V
        Resistors: [200, 44, 350, 3, 1200, 500], Voltage across LED: 0.06V
        Resistors: [200, 44, 350, 3, 500], Voltage across LED: 0.13V
        Resistors: [200, 44, 350, 3, 1200, 500], Voltage across LED: 0.06V
        Best combination of resistors: [500] with voltage across LED: 0.29V
        >>> 

