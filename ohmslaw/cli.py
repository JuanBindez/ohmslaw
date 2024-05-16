import argparse

from ohmslaw.__main__ import Ohms

class OhmsCLI:
    """Command line interface for Ohms calculations."""

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Perform electrical calculations based on Ohm\'s Law')
        self.subparsers = self.parser.add_subparsers(dest='operation', help='Operation to perform')

        # Subparser for volts operation
        volts_parser = self.subparsers.add_parser('volts', help='Calculate voltage using Ohm\'s Law')
        volts_parser.add_argument('-I', type=float, required=True, help='Current in amperes')
        volts_parser.add_argument('-R', type=float, required=True, help='Resistance in ohms')

        # Subparser for current operation
        current_parser = self.subparsers.add_parser('current', help='Calculate current using Ohm\'s Law')
        current_parser.add_argument('-V', type=float, required=True, help='Voltage in volts')
        current_parser.add_argument('-R', type=float, required=True, help='Resistance in ohms')

        # Subparser for resistance operation
        resistance_parser = self.subparsers.add_parser('resistance', help='Calculate resistance using Ohm\'s Law')
        resistance_parser.add_argument('-V', type=float, required=True, help='Voltage in volts')
        resistance_parser.add_argument('-I', type=float, required=True, help='Current in amperes')

        # Subparser for find_resistor operation
        find_resistor_parser = self.subparsers.add_parser('find_resistor', help='Calculate resistor value to limit current')
        find_resistor_parser.add_argument('--source', type=float, required=True, help='Source voltage in volts')
        find_resistor_parser.add_argument('--component_voltage', type=float, required=True, help='Component voltage in volts')
        find_resistor_parser.add_argument('--component_current', type=float, default=0.02, help='Component current in amperes (default: 0.02)')

    def main(self):
        args = self.parser.parse_args()
        ohms = Ohms()

        if args.operation == 'volts':
            result = ohms.volts(args.I, args.R)
        elif args.operation == 'current':
            result = ohms.current(args.V, args.R)
        elif args.operation == 'resistance':
            result = ohms.resistance(args.V, args.I)
        elif args.operation == 'find_resistor':
            result = ohms.find_resistor(args.source, args.component_voltage, args.component_current)

        print("Result:", result)

if __name__ == "__main__":
    cli = OhmsCLI()
    cli.main()

"""
    python cli.py volts -I 2 -R 4
    python cli.py current -V 10 -R 5
    python cli.py resistance -V 5 -I 2
    python cli.py find_resistor --source 10 --component_voltage 2

"""
