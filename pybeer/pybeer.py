import beer_data

class Beer:
	def __init__(self, name):
		self.name = name
		self.score = self.get_score(self.name)
		self.brewer = self.get_brewer(self.name)
		self.style = self.get_style(self.name)
		self.abv = self.get_abv(self.name)

	def get_abv(self, beer):
		raw = beer_data.beer_profile(beer)
		abv_pointer = raw.find('Style | ABV')
		abv_area = raw[abv_pointer:abv_pointer+100]
		abv_start = abv_area.find(';')
		abv_end = abv_area.find('%')
		abv = abv_area[abv_start+1:abv_end+1]
		return abv

	def get_style(self, beer):
		raw = beer_data.beer_profile(beer)
		style_pointer = raw.find('Style | ABV')
		style_area = raw[style_pointer:style_pointer+100]
		style_start = style_area.find("><b>")
		style_end = style_area.find("</b></a>")
		style = style_area[style_start+4:style_end]
		return style

	def get_brewer(self, beer):
		raw = beer_data.beer_profile(beer)
		brewer_pointer = raw.find("Brewed by")
		brewer_area = raw[brewer_pointer:brewer_pointer+150]
		brewer_start = brewer_area.find("<b>")
		brewer_end = brewer_area.find("</b></a>")
		brewer = brewer_area[brewer_start+3:brewer_end]
		return brewer

	def get_score(beer):
		raw = beer_profile(beer)
		score_pointer = raw.find("BAscore_big ba-score")
		score_area = raw[score_pointer:score_pointer+100]
		score_start = score_area.find(">")
		score_end = score_area.find("<")
		score = score_area[score_start+1:score_end]
		return score
