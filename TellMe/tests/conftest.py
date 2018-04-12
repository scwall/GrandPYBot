import pytest
import requests
import googlemaps
from flask import jsonify, request

from TellMe.views import create_app

@pytest.fixture(autouse=True)
def app(monkeypatch):

    def requests_return(url):
        links = {'https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&list='
                 '&generator=geosearch&utf8=1&exsentences=4&exintro=1&explaintext=1&exsectionformat=raw&'
                 'ggscoord=0.0|0.0': {'query':{'pages':{'key':{'extract': True}}}}}
        class FakeJson:
            def __init__(self,response):
                self.response = response
            def json(self):
                return self.response
        fake_json = FakeJson(links[url])
        return fake_json
    def googlemaps_return(key):
        class FakeGoogleMaps:
            def __init__(self,key):
                self.key = key
                self.coordinate = [{'geometry':{'location' : {'lat': 0.00, 'lng': 0.00}}}]
            def geocode(self,question):
                return self.coordinate
        fake_google_maps = FakeGoogleMaps(key)
        return fake_google_maps

    monkeypatch.setattr(googlemaps,'Client', googlemaps_return)
    monkeypatch.setattr(requests, 'get', requests_return)
    app = create_app('TellMe.tests.config')
    return app