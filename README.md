# beer-for-python

# Installation:

```python
pip install pybeer
```

# Example Usage

```python
from pybeer import pybeer

corona = pybeer.Beer('corona extra')

print corona.name #nothing fancy, you just typed it above
print corona.brewer #the brewer of the beer
print corona.style #the style of the beer
print corona.abv #the ABV (alcohol by volume) of the beer
```

alternatively, 

```python
from pybeer import beer_data

data = beer_data.Engine()
data.get_brewer('coors light')
data.get_style('coors light')
data.get_abv('coors light')
```
