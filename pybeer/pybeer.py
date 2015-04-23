import re

from BeautifulSoup import BeautifulSoup as bs

import beer_data
import bad_beer as errors

class Beer:
    def __init__(self, name):
        try:
            self.name = name.title()

            #keep the raw html, because some things may be easier to regex for
            self._html = beer_data.beer_profile_html(name)
            self._soup = bs(self._html)

            #so that things don't break in the interim
            self.raw_profile = self._html
            
            self.score = self.get_score()               #TODO
            self.brewer = self.get_brewer()             #DONE
            self.style = self.get_style()               #DONE
            self.abv = self.get_abv()                   #DONE
            
            self.description = self.get_description()   #TODO
        except errors.Invalid_Beer as error:
            print(error.args[0])
        except AttributeError:
            #This is never reached from this try block, I think?
            print("you are trying to call a data retrieval method"
                  "on a beer that could not be found")

    def __repr__(self):
            return "{}(\"{}\")".format(
                    self.__class__.__name__,
                    self.name)

    def get_abv(self):
        styleabv = self._soup.firstText("Style | ABV")
        text = styleabv.parent.parent.getText()

        abv = re.search(r'([0-9.]+%)ABV', text)

        #what about beers with multiple styles? (TODO)
        #NB: I haven't found an example of that yet
        return abv.groups()[0]

    def get_style(self):
        styleabv = self._soup.firstText("Style | ABV")
        style = styleabv.findNext('b').getText()

        return style

    def get_brewer(self):
        brewed_by_text = self._soup.firstText("Brewed by:")
        brewer = brewed_by_text.findNext('b').getText()

        return brewer

    def get_score(self):
        raw = self.raw_profile
        score_pointer = raw.find("BAscore_big ba-score")
        score_area = raw[score_pointer:score_pointer+100]
        score_start = score_area.find(">")
        score_end = score_area.find("<")
        score = score_area[score_start+1:score_end]
        return score

    def get_description(self):
        raw = self.raw_profile
        desc_pointer = raw.find("Commercial Description")
        desc_area = raw[desc_pointer:]
        desc_start = desc_area.find("<br><br>")
        desc_end = desc_area.find("</td>")
        description = desc_area[desc_start+8:desc_end]
        return description
