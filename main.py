from ohmslaw import Ohms

o = Ohms()
results = o.find_resistor(source=48, component_voltage=12)

print(results)