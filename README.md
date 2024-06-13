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

### current multiplied by resistance = voltage

```python

o = Ohms()
results = o.volts(2, 4)

print(results)

```

### voltage Divided by resistance = current

```python

o = Ohms()
results = o.current(12, 4)

print(results)

```

### voltage divided by current = resistance

```python

o = Ohms()
results = o.resistance(48, 4)

print(results)

```

### find the resistance value to limit the electrical voltage of a circuit

```python

o = Ohms()
results = o.find_resistor(source=48, component_voltage=12)# Led

print(results)

```
