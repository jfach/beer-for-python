import beer_data

class Beer:
	def __init__(self, name):
		self.data = beer_data.Engine()
		self.name = name
		self.brewer = self.data.get_brewer(self.name)
		self.style = self.data.get_style(self.name)
		self.abv = self.data.get_abv(self.name)




