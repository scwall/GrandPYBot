import datetime
from typing import Optional, List

import googlemaps
import requests

from TellMe.packages.parser import Parser

"""
The TelleMe class will allow the search for coordinates on googlemaps after the question is passed to the text parser, 
the coordinates can then be sent to wikipedia for a search on an area known to it. 
The construction of the object will take as parameter in the constructor the googlemaps key
"""

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
        self.wikipedia_link_get_long_range = "https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&" \
                                             "generator=geosearch&utf8=1&exsentences=4&exintro=1&explaintext=1" \
                                             "&ggscoord={coordinates}&ggsradius=10000&ggsglobe=earth"

    def google_map(self):
        """
            Function that will allow the search of the location on googlemaps,
            if there is no information found it returns false
        """
        try:
            geocode_result = self.gmaps.geocode(self._question)
            self._googlemaps_geocode_result = geocode_result[0]['geometry']['location']
        except:
            return False

    def wikipedia(self):
        """
            Function that will search on wikipedia according to the coordinates received from googlemaps
            If the coordinates do not give a history on the place then it is returned on a longer search range
        """

        reply = requests.get(self.wikipedia_link_get.format(
            coordinates=str(self._googlemaps_geocode_result['lat']) + "|" + str(
                self._googlemaps_geocode_result['lng'])))
        reply = reply.json()
        if 'query' is not reply.keys():
            reply = requests.get(self.wikipedia_link_get_long_range.format(
                coordinates=str(self._googlemaps_geocode_result['lat']) + "|" + str(
                    self._googlemaps_geocode_result['lng'])))
            reply = reply.json()
            key = str(next(iter(reply['query']['pages'])))
            self._wikipedia_result = reply['query']['pages'][key]['extract']
        else:
            key = str(next(iter(reply['query']['pages'])))
            self._wikipedia_result = reply['query']['pages'][key]['extract']

    def set_question(self, question):
        self._question = self.parser.parser_word(question)

    def get_googlemaps_geocode_result(self):
        return self._googlemaps_geocode_result

    def get_wikipedia_result(self):
        return self._wikipedia_result

    def get_last_version_groups_for_content_cycle(cls, content_cycle_id: int) -> int:
        pass

    def patate(self):
        test = self.get_last_version_groups_for_content_cycle("test")
