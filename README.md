# beer-for-python

# Description

PyBeer is my solution to BeerAdvocate.com's lack of any sort of API. BeerAdvocate is a great resource, and has tons of quality data on a large variety of beers. Right now PyBeer utlizes mechanize, but most likely will not in the near future. This project is still in development, and while it is usable, should in no way shape or form be considered a completed package. 


# Installation:

```python
pip install pybeer
```

# Example Usage

```python
from pybeer import pybeer

beer = pybeer.Beer
beer.get_brewer('coors light')
beer.get_style('corona extra')
beer.get_abv('modelo especiale')
```
Alternatively, you can just make an instance of a class and pass in the name of a beer as a string, and __init__ will gather the data for your beer.
```python
from pybeer import pybeer

corona = pybeer.Beer('corona extra')

print corona.name #nothing fancy, you just typed it above
print corona.brewer #the brewer of the beer
print corona.style #the style of the beer
print corona.abv #the ABV (alcohol by volume) of the beer
```

