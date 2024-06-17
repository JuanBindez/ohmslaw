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

def calculate_series(*resistors):
    """Calculate total resistance for resistors in series."""
    ohms = Ohms()
    return ohms.series(*resistors)

def calculate_parallel(*resistors):
    """Calculate total resistance for resistors in parallel."""
    ohms = Ohms()
    return ohms.parallel(*resistors)

def calculate_best_combination(source_voltage, component_voltage, component_current, resistors):
    """Find the best combination of resistors."""
    ohms = Ohms()
    return ohms.best_combination(source_voltage, component_voltage, component_current, resistors)

def main() -> str:
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

    watts_parser = subparsers.add_parser('watts', help='Calculate watts using Ohm\'s Law')
    watts_parser.add_argument('-R', type=float, required=True, help='Resistance in ohms')
    watts_parser.add_argument('-I', type=float, required=True, help='Current in amperes')

    # Subparser for find_resistor operation
    find_resistor_parser = subparsers.add_parser('find_resistor', help='Calculate resistor value to limit current')
    find_resistor_parser.add_argument('--source', type=float, required=True, help='Source voltage in volts')
    find_resistor_parser.add_argument('--component_voltage', type=float, required=True, help='Component voltage in volts')
    find_resistor_parser.add_argument('--component_current', type=float, default=0.02, help='Component current in amperes (default: 0.02)')

    # Subparser for series operation
    series_parser = subparsers.add_parser('series', help='Calculate total resistance for resistors in series')
    series_parser.add_argument('resistors', type=float, nargs='+', help='List of resistances in ohms')

    # Subparser for parallel operation
    parallel_parser = subparsers.add_parser('parallel', help='Calculate total resistance for resistors in parallel')
    parallel_parser.add_argument('resistors', type=float, nargs='+', help='List of resistances in ohms')

    # Subparser for best_combination operation
    best_combination_parser = subparsers.add_parser('best_combination', help='Find the best combination of resistors')
    best_combination_parser.add_argument('-sv', '--source_voltage', type=float, required=True, help='Source voltage in volts')
    best_combination_parser.add_argument('-cv', '--component_voltage', type=float, required=True, help='Component voltage in volts')
    best_combination_parser.add_argument('-cc', '--component_current', type=float, required=True, help='Component current in amperes')
    best_combination_parser.add_argument('-r', '--resistors', type=float, nargs='+', required=True, help='List of available resistors in ohms')

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
    elif args.operation == 'series':
        result = str(calculate_series(*args.resistors)) + " Ohms"
    elif args.operation == 'parallel':
        result = str(calculate_parallel(*args.resistors)) + " Ohms"
    elif args.operation == 'best_combination':
        combination, voltage = calculate_best_combination(args.source_voltage, args.component_voltage, args.component_current, args.resistors)
        result = f"Best combination: {combination} with voltage: {voltage} V"

    return result

if __name__ == "__main__":
    main()
