import argparse
from ohmslaw.__main__ import Ohms


def calculate_volts(I, R):
    """Calculate voltage using Ohm's Law."""
    ohms = Ohms()
    return ohms.volts(I, R)

def calculate_current(V, R):
    """Calculate current using Ohm's Law."""
    ohms = Ohms()
    return ohms.current(V, R)

def calculate_resistance(V, I):
    """Calculate resistance using Ohm's Law."""
    ohms = Ohms()
    return ohms.resistance(V, I)

def calculate_watts(I, R):
    """Calculate Watts."""
    ohms = Ohms()
    return ohms.watts(I, R)

def find_resistor(source, component_voltage, component_current=0.02):
    """Calculate resistor value to limit current."""
    ohms = Ohms()
    return ohms.find_resistor(source, component_voltage, component_current)

def main() -> str:
    import argparse
    parser = argparse.ArgumentParser(description="Perform electrical calculations based on Ohm's Law")
    subparsers = parser.add_subparsers(dest='operation', help='Operation to perform')

    # Subparser for volts operation
    volts_parser = subparsers.add_parser('volts', help='Calculate voltage using Ohm\'s Law')
    volts_parser.add_argument('-I', type=float, required=True, help='Current in amperes')
    volts_parser.add_argument('-R', type=float, required=True, help='Resistance in ohms')

    # Subparser for current operation
    current_parser = subparsers.add_parser('current', help='Calculate current using Ohm\'s Law')
    current_parser.add_argument('-V', type=float, required=True, help='Voltage in volts')
    current_parser.add_argument('-R', type=float, required=True, help='Resistance in ohms')

    # Subparser for resistance operation
    resistance_parser = subparsers.add_parser('resistance', help='Calculate resistance using Ohm\'s Law')
    resistance_parser.add_argument('-V', type=float, required=True, help='Voltage in volts')
    resistance_parser.add_argument('-I', type=float, required=True, help='Current in amperes')

    watts_parser = subparsers.add_parser('watts', help='Calculate watts\'s Law')
    watts_parser.add_argument('-R', type=float, required=True, help='Resistance in amperes')
    watts_parser.add_argument('-I', type=float, required=True, help='Current in amperes')

    # Subparser for find_resistor operation
    find_resistor_parser = subparsers.add_parser('find_resistor', help='Calculate resistor value to limit current')
    find_resistor_parser.add_argument('--source', type=float, required=True, help='Source voltage in volts')
    find_resistor_parser.add_argument('--component_voltage', type=float, required=True, help='Component voltage in volts')
    find_resistor_parser.add_argument('--component_current', type=float, default=0.02, help='Component current in amperes (default: 0.02)')

    args = parser.parse_args()

    result = None

    if args.operation == 'volts':
        result = str(calculate_volts(args.I, args.R)) + " V"
    elif args.operation == 'current':
        result = str(calculate_current(args.V, args.R)) + " A"
    elif args.operation == 'resistance':
        result = str(calculate_resistance(args.V, args.I)) + " Ohms"
    elif args.operation == 'watts':
        result = str(calculate_watts(args.R, args.I)) + " Watts"
    elif args.operation == 'find_resistor':
        result = str(find_resistor(args.source, args.component_voltage, args.component_current)) + " Ohms"

    return result

if __name__ == "__main__":
    main()


"""
    python cli.py volts -I 2 -R 4
    python cli.py current -V 10 -R 5
    python cli.py resistance -V 5 -I 2
    python cli.py find_resistor --source 10 --component_voltage 2

"""
