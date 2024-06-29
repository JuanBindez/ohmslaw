from itertools import combinations


class Ohms:
    """A class representing basic electrical calculations based on Ohm's Law."""
    
    def volts(self, I: float, R: float) -> float:
        """
        Calculate voltage using Ohm's Law.

        Parameters:
            I (float): The current in amperes.
            R (float): The resistance in ohms.

        Returns:
            float: The voltage in volts.
        """
        V = I * R
        return V
    
    def current(self, V: float, R: float) -> float:
        """
        Calculate current using Ohm's Law.

        Parameters:
            V (float): The voltage in volts.
            R (float): The resistance in ohms.

        Returns:
            float: The current in amperes.
        """
        I = V / R
        return I
        
    def resistance(self, V: float, I: float) -> float:
        """
        Calculate resistance using Ohm's Law.

        Parameters:
            V (float): The voltage in volts.
            I (float): The current in amperes.

        Returns:
            float: The resistance in ohms.
        """
        R = V / I
        return R
    
    def watts(self, I: float, R: float) -> float:
        """
        Calculate electrical power in watts using current and resistance.

        This method uses the formula P = I^2 * R to calculate electrical power,
        where P is the power in watts, I is the current in amperes, and R is the
        resistance in ohms.

        Parameters:
        -----------
        I : float
            Electrical current in amperes (A).
        R : float
            Electrical resistance in ohms (Ω).

        Returns:
        --------
        float
            Electrical power in watts (W).

        Example:
        --------
        >>> calculator = Ohms()
        >>> power = calculator.watts(3.0, 5.0)
        >>> print(power)
        45.0
        """
        W = I**2 * R
        return W
    
    def find_resistor(self, 
                  source: float,
                  component_voltage: float,
                  component_current: float = 0.02 # initial value for LED, change the value for other components
                  ) -> float:
        """
        Calculate the resistor value needed to limit the current flowing through a component using Ohm's Law.

        This method calculates the resistor value needed to limit the current flowing through a component
        to a specified value, considering the source voltage and the forward voltage drop of the component.

        Parameters:
            source (float): The voltage of the power source in volts.
            component_voltage (float): The forward voltage drop of the component in volts.
            component_current (float): The desired current for the component in amperes.

        Returns:
            float: The resistance value needed for the circuit in ohms.
        """
        
        U = source - component_voltage  # Calcula a tensão sobre o resistor
        R = U / component_current       # Calcula a resistência usando a Lei de Ohm
        return R

    
    def series(self, *resistors: float) -> float:
        """
        Calculate the total resistance of resistors in series.

        Parameters:
            resistors (float): Resistances of the resistors in ohms.

        Returns:
            float: The total resistance in ohms.
        """
        return sum(resistors)
    
    def parallel(self, *resistors: float) -> float:
        """
        Calculate the total resistance of resistors in parallel.

        Parameters:
            resistors (float): Resistances of the resistors in ohms.

        Returns:
            float: The total resistance in ohms.
        """
        inverse_total_resistance = sum(1/r for r in resistors)
        return 1 / inverse_total_resistance
    
    def best_combination(self, source_voltage: float, component_voltage: float, component_current: float, resistors: list) -> tuple:
        """
        Find the best combination of resistors to achieve the desired voltage drop across the component.

        Parameters:
            source_voltage (float): The voltage of the power source in volts.
            component_voltage (float): The desired voltage drop across the component in volts.
            component_current (float): The desired current for the component in amperes.
            resistors (list): A list of available resistors in ohms.

        Returns:
            tuple: The best combination of resistors and the resulting voltage across the component.
        """
        best_combination = None
        closest_voltage = float('inf')
        target_voltage = source_voltage - component_voltage

        for r in range(1, len(resistors) + 1):
            for combo in combinations(resistors, r):
                total_resistance = self.series(*combo)
                total_current = source_voltage / (total_resistance + (component_voltage / component_current))
                voltage_drop_across_resistors = total_current * total_resistance
                voltage_across_component = source_voltage - voltage_drop_across_resistors
                if abs(voltage_across_component - component_voltage) < abs(closest_voltage - component_voltage):
                    closest_voltage = voltage_across_component
                    best_combination = combo

        return best_combination, closest_voltage

