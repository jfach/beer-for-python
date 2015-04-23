import re
import requests
import bad_beer

main_url = "http://www.beeradvocate.com"
beer_url_re = re.compile(r'/beer/profile/[0-9]+/[0-9]+/?')

def generate_link(beer):
    beer_name = beer.replace(" ", "+")
    query = main_url + "/search/?q={}&qt=beer".format(beer_name)
    
    return query

def find_beer_link(beer):
    url = generate_link(beer)

    response = requests.get(url)

    links = beer_url_re.findall(response.text)

    #links is either empty, or a list of valid links
    #how do we decide which one? Do we assume the first one?
    #That's what we'll do for now (TODO)

    if links:
        return main_url + links[0]

    raise bad_beer.Invalid_Beer("ERROR: [{}] not found. "
                "Did you check the spelling/name?".format(beer))

def beer_profile(beer):
    beer_page = find_beer_link(beer)
    response = requests.get(beer_page)
    
    #should we soup up here? It would mean importing BS just for one call
    return response.text



