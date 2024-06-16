# ohmslaw

![PyPI - Downloads](https://img.shields.io/pypi/dm/ohmslaw)
![PyPI - License](https://img.shields.io/pypi/l/ohmslaw)
[![Documentation Status](https://readthedocs.org/projects/ohmslaw/badge/?version=latest)](https://ohmslaw.readthedocs.io/en/latest/?badge=latest)
![GitHub Tag](https://img.shields.io/github/v/tag/JuanBindez/ohmslaw?include_prereleases&link=https%3A%2F%2Fgithub.com%2FJuanBindez%2Fohmslaw%2Ftags)
<a href="https://pypi.org/project/ohmslaw/"><img src="https://img.shields.io/pypi/v/ohmslaw" /></a>


#### Ohms law is an important and fundamental rule to remember when working with resistors and electronics in general. It defines the relationship between the components’ current I in amps (A), voltage V in volts (V) and resistance R in ohms (Ω). Ohm’s law consists of three mathematical equations that explain the relationship between current, voltage and resistance. If you know two of these values.

## Quickstart:

### install

    pip install ohmslaw

### import

```python
from ohmslaw import Ohms
```

### Combinations of Resistors

```python
>>> 
>>> LED_VOLTAGE = 3
>>> SOURCE_VOLTAGE = 48
>>> 
>>> resistors = [200, 44, 350, 3, 1200, 500]
>>> 
>>> o = Ohms()
>>> 
>>> def calculate_voltage(selected_resistors):
...     total_resistance = o.series(*selected_resistors)
...     total_current = SOURCE_VOLTAGE / total_resistance
...     led_voltage = total_current * LED_VOLTAGE
...     return led_voltage
... 
>>> # Testing different combinations of resistors
>>> for i in range(len(resistors)):
...     for j in range(i, len(resistors)):
...         combination = resistors[:i] + resistors[j:]
...         voltage = calculate_voltage(combination)
...         print(f"Resistors: {combination}, Voltage across LED: {voltage:.2f}V")
... 
>>> # Checking the closest combination for 3V across the LED
>>> best_combination = None
>>> smallest_difference = float('inf')
>>> 
>>> for i in range(len(resistors)):
...     for j in range(i, len(resistors)):
...         combination = resistors[:i] + resistors[j:]
...         voltage = calculate_voltage(combination)
...         difference = abs(voltage - LED_VOLTAGE)
...         if difference < smallest_difference:
...             smallest_difference = difference
...             best_combination = combination
... 
>>> print(f"Best combination of resistors: {best_combination} with voltage across LED: {calculate_voltage(best_combination):.2f}V")
Resistors: [200, 44, 350, 3, 1200, 500], Voltage across LED: 0.06V
Resistors: [44, 350, 3, 1200, 500], Voltage across LED: 0.07V
Resistors: [350, 3, 1200, 500], Voltage across LED: 0.07V
Resistors: [3, 1200, 500], Voltage across LED: 0.08V
Resistors: [1200, 500], Voltage across LED: 0.08V
Resistors: [500], Voltage across LED: 0.29V
Resistors: [200, 44, 350, 3, 1200, 500], Voltage across LED: 0.06V
Resistors: [200, 350, 3, 1200, 500], Voltage across LED: 0.06V
Resistors: [200, 3, 1200, 500], Voltage across LED: 0.08V
Resistors: [200, 1200, 500], Voltage across LED: 0.08V
Resistors: [200, 500], Voltage across LED: 0.21V
Resistors: [200, 44, 350, 3, 1200, 500], Voltage across LED: 0.06V
Resistors: [200, 44, 3, 1200, 500], Voltage across LED: 0.07V
Resistors: [200, 44, 1200, 500], Voltage across LED: 0.07V
Resistors: [200, 44, 500], Voltage across LED: 0.19V
Resistors: [200, 44, 350, 3, 1200, 500], Voltage across LED: 0.06V
Resistors: [200, 44, 350, 1200, 500], Voltage across LED: 0.06V
Resistors: [200, 44, 350, 500], Voltage across LED: 0.13V
Resistors: [200, 44, 350, 3, 1200, 500], Voltage across LED: 0.06V
Resistors: [200, 44, 350, 3, 500], Voltage across LED: 0.13V
Resistors: [200, 44, 350, 3, 1200, 500], Voltage across LED: 0.06V
Best combination of resistors: [500] with voltage across LED: 0.29V
>>> 

```


### current multiplied by resistance = voltage

```python
>>> o = Ohms()
>>> results = o.volts(I=12, R=4)
>>> 
>>> print(results)
48
>>> 

```

### voltage Divided by resistance = current

```python
>>> o = Ohms()
>>> results = o.current(V=12, R=4)
>>> 
>>> print(results)
3.0
>>> 
```

### voltage divided by current = resistance

```python
>>> o = Ohms()
>>> results = o.resistance(V=48, I=4)
>>> 
>>> print(results)
12.0
>>> 

```

### Watts

```python
>>> o = Ohms()
>>> results = o.watts(I=2, R=15)
>>> 
>>> print(results)
60
>>> 

```

### find the resistance value to limit the electrical voltage of a circuit

```python

>>> o = Ohms()
>>> results = o.find_resistor(source=48, 
...                           component_voltage=12,
...                           component_current=1)
>>> 
>>> print(results)
36.0
>>> 

```
