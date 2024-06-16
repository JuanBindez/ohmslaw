from ohmslaw import Ohms

# Defining constants
LED_VOLTAGE = 3
SOURCE_VOLTAGE = 48

# List of available resistors
resistors = [200, 44, 350, 3, 1200, 500]

# Initializing the Ohms object
o = Ohms()

def calculate_voltage(selected_resistors):
    # Calculating the total resistance of resistors in series
    total_resistance = o.series(*selected_resistors)
    # Calculating the total current using the 48V source
    total_current = SOURCE_VOLTAGE / total_resistance
    # Calculating the voltage across the LED (V = I * R)
    led_voltage = total_current * LED_VOLTAGE
    return led_voltage

# Testing different combinations of resistors
for i in range(len(resistors)):
    for j in range(i, len(resistors)):
        combination = resistors[:i] + resistors[j:]
        voltage = calculate_voltage(combination)
        print(f"Resistors: {combination}, Voltage across LED: {voltage:.2f}V")

# Checking the closest combination for 3V across the LED
best_combination = None
smallest_difference = float('inf')

for i in range(len(resistors)):
    for j in range(i, len(resistors)):
        combination = resistors[:i] + resistors[j:]
        voltage = calculate_voltage(combination)
        difference = abs(voltage - LED_VOLTAGE)
        if difference < smallest_difference:
            smallest_difference = difference
            best_combination = combination

print(f"Best combination of resistors: {best_combination} with voltage across LED: {calculate_voltage(best_combination):.2f}V")
