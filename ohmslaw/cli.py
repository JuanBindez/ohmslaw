import argparse

class OhmsCLI:
    """Command line interface for Ohms calculations."""

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Perform electrical calculations based on Ohm\'s Law')
        self.parser.add_argument('operation', choices=['volts', 'current', 'resistance', 'find_resistor'], help='The operation to perform')
        self.parser.add_argument('-V', type=float, help='Voltage in volts')
        self.parser.add_argument('-I', type=float, help='Current in amperes')
        self.parser.add_argument('-R', type=float, help='Resistance in ohms')
        self.parser.add_argument('--source', type=float, help='Source voltage in volts')
        self.parser.add_argument('--component_voltage', type=float, help='Component voltage in volts')
        self.parser.add_argument('--component_current', type=float, default=0.02, help='Component current in amperes (default: 0.02)')

    def run(self):
        args = self.parser.parse_args()
        ohms = Ohms()
        
        if args.operation == 'volts':
            if args.I is not None and args.R is not None:
                result = ohms.volts(args.I, args.R)
            else:
                print("Error: Voltage calculation requires both current (I) and resistance (R) values.")
                return
        elif args.operation == 'current':
            if args.V is not None and args.R is not None:
                result = ohms.current(args.V, args.R)
            else:
                print("Error: Current calculation requires both voltage (V) and resistance (R) values.")
                return
        elif args.operation == 'resistance':
            if args.V is not None and args.I is not None:
                result = ohms.resistance(args.V, args.I)
            else:
                print("Error: Resistance calculation requires both voltage (V) and current (I) values.")
                return
        elif args.operation == 'find_resistor':
            if args.source is not None and args.component_voltage is not None:
                result = ohms.find_resistor(args.source, args.component_voltage, args.component_current)
            else:
                print("Error: Find resistor calculation requires source voltage and component voltage.")
                return
        else:
            print("Error: Invalid operation.")
            return
        
        print("Result:", result)

if __name__ == "__main__":
    cli = OhmsCLI()
    cli.run()
