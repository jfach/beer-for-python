import mechanize

search = mechanize.Browser()
search.set_handle_robots(False)
search.addheaders = [("User-agent", 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)')]

def generate_link(beer):
	beer_name = beer.replace(" ", "+")
	query = "http://www.beeradvocate.com/search/?q={}&qt=beer".format(beer_name)
	return query

def find_beer_link(beer):
	url = generate_link(beer)
	search.open(url)
	for link in search.links():
		if str(link.text).lower() == beer.lower():
			return link.url

def beer_profile(beer):
	beer_page = find_beer_link(beer)
	response = search.open(beer_page)
	raw = response.read()
	return raw



