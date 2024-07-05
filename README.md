# ohmslaw

![PyPI - Downloads](https://img.shields.io/pypi/dm/ohmslaw)
![PyPI - License](https://img.shields.io/pypi/l/ohmslaw)
[![Documentation Status](https://readthedocs.org/projects/ohmslaw/badge/?version=latest)](https://ohmslaw.readthedocs.io/en/latest/?badge=latest)
![GitHub Tag](https://img.shields.io/github/v/tag/JuanBindez/ohmslaw?include_prereleases&link=https%3A%2F%2Fgithub.com%2FJuanBindez%2Fohmslaw%2Ftags)
<a href="https://pypi.org/project/ohmslaw/"><img src="https://img.shields.io/pypi/v/ohmslaw" /></a>

### Python3 library for calculations using Ohm's law 

#### Ohms law is an important and fundamental rule to remember when working with resistors and electronics in general. It defines the relationship between the components’ current I in amps (A), voltage V in volts (V) and resistance R in ohms (Ω). Ohm’s law consists of three mathematical equations that explain the relationship between current, voltage and resistance. If you know two of these values.

## Quickstart:

### install

    pip install ohmslaw

### import

```python
from ohmslaw import Ohms
```

### you can calculate the resistors in series, passing the values ​​in the series() method

```python
>>> from ohmslaw import Ohms
>>>
>>> R1, R2, R3 = 280, 450, 100
>>>
>>> o = Ohms()
>>> series = o.series(R1, R2, R3)
>>>
>>> print("Resistors in series = ", series)
Resistors in series =  830
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