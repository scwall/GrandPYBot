import googlemaps
import wikipediaapi
from bin.Parser.parser import Parser


class TellMe:
    def __init__(self, googlemapapikey):
        self._googlemaps_result = dict()
        self._googlemaps_formatted_address = str()
        self._wikipedia_result = dict()
        self._question = str()
        self.gmaps = googlemaps.Client(key=googlemapapikey)
        self.parser = Parser(language='fr')
    def google_map(self):
        test_correct = False
        while test_correct is False:
            geocode_result = self.gmaps.geocode(self._question)
            print(self._question)
            self._googlemaps_formatted_address = self.parser.parser_number(geocode_result[0]['formatted_address'])
            return geocode_result[0]['geometry']['location']

    def wikipedia(self):
        wiki_wiki = wikipediaapi.Wikipedia('fr')
        try_research = False
        while try_research is False:
            self._wikipedia_result = wiki_wiki.page(self._googlemaps_formatted_address)
            try_research = self._wikipedia_result.exists()
            self._googlemaps_formatted_address = self.parser.parser_refine(self._googlemaps_formatted_address,method='reverse')


        return self._wikipedia_result

    def set_question(self, question):
        
        self._question = self.parser.parser_word(question)




#parser = Parser('fr')
#question2 = parser.parser_word(question)
#print(question2)
tellme = TellMe("AIzaSyC_0sMqi7mbdoquIuAX8_GpyRuGrNu88qI")

tellme.set_question(question)

tellme.wikipedia()
