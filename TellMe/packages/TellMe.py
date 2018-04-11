import googlemaps
import requests
from flask import json

from bin.Parser.parser import Parser


class TellMe:
    def __init__(self, googlemapapikey):
        self._googlemaps_result = dict()
        self._googlemaps_formatted_address = str()
        self._googlemaps_geocode_result = dict()
        self._wikipedia_result = dict()
        self._question = str()
        self.gmaps = googlemaps.Client(key=googlemapapikey)
        self.parser = Parser(language='fr')
        self.wikipedia_link_get = "https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&" \
                                  "list=&generator=geosearch&utf8=1&exsentences=4&exintro=1&explaintext=1&" \
                                  "exsectionformat=raw&ggscoord={coordinates}"

    def google_map(self):
        test_correct = False
        while test_correct is False:
            geocode_result = self.gmaps.geocode(self._question)
            self._googlemaps_formatted_address = self.parser.parser_number(geocode_result[0]['formatted_address'])
            self._googlemaps_geocode_result = geocode_result[0]['geometry']['location']
            test_correct = True
        return self._googlemaps_geocode_result

    def wikipedia(self):
        reply = requests.get(self.wikipedia_link_get.format(
            coordinates=str(self._googlemaps_geocode_result['lat']) + "|" + str(
                self._googlemaps_geocode_result['lng'])))
        reply = reply.json()
        self.reply = reply
        key = str(next(iter(self.reply['query']['pages'])))
        return self.reply['query']['pages'][key]['extract']

    def set_question(self, question):
        self._question = self.parser.parser_word(question)


tellme = TellMe("AIzaSyC_0sMqi7mbdoquIuAX8_GpyRuGrNu88qI")

tellme.set_question("openclassrooms ")
print(tellme.google_map())
print(tellme.wikipedia())