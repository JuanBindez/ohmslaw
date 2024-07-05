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
