# beer-for-python

# Description

PyBeer is my solution to BeerAdvocate.com's lack of any sort of API. BeerAdvocate is a great resource, and has tons of quality data on a large variety of beers. Right now PyBeer utlizes mechanize, but most likely will not in the near future. This project is still in development, and while it is usable, should in no way shape or form be considered a completed package. 


# Installation:

```python
pip install pybeer
```

# Example Usage

Just make an instance of the Beer class and pass in the name of a beer as a string, and __init__ will gather the data for your beer.
```python
from pybeer import pybeer

my_beer = pybeer.Beer('corona extra')

print my_beer.name # name of the beer, which you set above
print my_beer.brewer # the brewer of the beer
print my_beer.style # the type/style this beer is considered
print my_beer.abv # the ABV (alcohol by volume)
print my_beer.score # average score on BA, averaged from thousands of users
```

