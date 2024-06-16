from ohmslaw import Ohms

o = Ohms()

SOURCE_VOLTAGE = 48
COMPONENT_VOLTAGE = 3
COMPONENT_CURRENT = 0.02  # Desired current for the component (e.g., LED)

resistors = [200, 44, 350, 3, 1200, 500]

best_combination, resulting_voltage = o.best_combination(SOURCE_VOLTAGE, COMPONENT_VOLTAGE, COMPONENT_CURRENT, resistors)

print(f"Best combination of resistors: {best_combination}")
print(f"Resulting voltage on the component: {resulting_voltage:.2f}V")
