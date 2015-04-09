import mechanize


class Engine:

	def __init__(self):
		self.search = mechanize.Browser()
		self.search.set_handle_robots(False)
		self.search.addheaders = [("User-agent", 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)')]

	def generate_link(self, beer):
		beer_name = beer.replace(" ", "+")
		query = "http://www.beeradvocate.com/search/?q={}&qt=beer".format(beer_name)
		return query

	def find_beer_link(self, beer):
		url = self.generate_link(beer)
		self.search.open(url)
		for link in self.search.links():
			if str(link.text).lower() == beer.lower():
				return link.url

	def beer_profile(self, beer):
		beer_page = self.find_beer_link(beer)
		response = self.search.open(beer_page)
		raw = response.read()
		return raw

	def get_abv(self, beer):
		raw = self.beer_profile(beer)
		abv_pointer = raw.find('Style | ABV')
		abv_area = raw[abv_pointer:abv_pointer+100]
		abv_start = abv_area.find(';')
		abv_end = abv_area.find('%')
		abv = abv_area[abv_start+1:abv_end+1]
		return abv

	def get_style(self, beer):
		raw = self.beer_profile(beer)
		style_pointer = raw.find('Style | ABV')
		style_area = raw[style_pointer:style_pointer+100]
		style_start = style_area.find("><b>")
		style_end = style_area.find("</b></a>")
		style = style_area[style_start+4:style_end]
		return style

	def get_brewer(self, beer):
		raw = self.beer_profile(beer)
		brewer_pointer = raw.find("Brewed by")
		brewer_area = raw[brewer_pointer:brewer_pointer+150]
		brewer_start = brewer_area.find("<b>")
		brewer_end = brewer_area.find("</b></a>")
		brewer = brewer_area[brewer_start+3:brewer_end]
		return brewer	