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
    
    def find_resistor(self, 
                    source: float,
                    component_voltage: float,
                    component_current: float = 0.02 # initial velue for LED, change the velue in another componets
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
        
        
        U = source - component_voltage
        R = U / component_current
        return R
