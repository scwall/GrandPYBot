import os
import pytest
import googlemaps
import pytest
import requests
from TellMe import models
from TellMe.packages import questionSearch
from TellMe.models import LoadSiteResponseGrandPy
from TellMe.views import create_app
basedir = os.path.abspath(os.path.dirname(__file__))
"""
Patch requests and googlemaps functions to return a value even 
if there is no connection to the external service
"""


@pytest.fixture(autouse=True)
def app(monkeypatch):
    print('avant')
    def requests_return(url):
        links = {'https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&list='
                 '&generator=geosearch&utf8=1&exsentences=4&exintro=1&explaintext=1&exsectionformat=raw&'
                 'ggscoord=0.0|0.0': {'query': {'pages': {'key': {'extract': True}}}}}

        class FakeJson:
            def __init__(self, response):
                self.response = response

            def json(self):
                return self.response

        fake_json = FakeJson(links['https://fr.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&list='
                                   '&generator=geosearch&utf8=1&exsentences=4&exintro=1&explaintext=1&exsectionformat=raw&'
                                   'ggscoord=0.0|0.0'])
        return fake_json

    def googlemaps_return(key):
        class FakeGoogleMaps:
            def __init__(self, key):
                self.key = key
                self.coordinate = [{'geometry': {'location': {'lat': 0.00, 'lng': 0.00}}}]

            def geocode(self, question):
                return self.coordinate

        fake_google_maps = FakeGoogleMaps(key)
        return fake_google_maps


    monkeypatch.setattr(googlemaps, 'Client', googlemaps_return)
    monkeypatch.setattr(requests, 'get', requests_return)
    app = create_app('TellMe.tests.config')
    return app


@pytest.fixture()
def db(app):
    print('test')
    models.db.drop_all()
    models.db.create_all()
    models.db.session.add(
        models.ResponseGrandPy(
            "Huh, je vais te raconter une histoire sur cette endroit "))
    models.db.session.add(models.ResponseGrandPy(
        "Je vais te compter une histoire de mon souvenir "))
    models.db.session.add(models.LoadSiteResponseGrandPy("Pose moi une question"))
    models.db.session.add(models.LoadSiteResponseGrandPy("Je suis à ton écoute"))
    models.db.session.add(models.ResponseGrandPyError("PARLE PLUS FORT ! Je n'ai pas compris la question "))
    models.db.session.commit()

# @pytest.fixture(scope="session", autouse=True)
# def my_own_session_run_at_beginning(request):
#     print('création database')
#     models.db.drop_all()
#     models.db.create_all()
#     models.db.session.add(
#         models.ResponseGrandPy(
#             "Huh, je vais te raconter une histoire sur cette endroit "))
#     models.db.session.add(models.ResponseGrandPy(
#         "Je vais te compter une histoire de mon souvenir "))
#     models.db.session.add(models.LoadSiteResponseGrandPy("Pose moi une question"))
#     models.db.session.add(models.LoadSiteResponseGrandPy("Je suis à ton écoute"))
#     models.db.session.add(models.ResponseGrandPyError("PARLE PLUS FORT ! Je n'ai pas compris la question "))
#     models.db.session.commit()
#     def my_own_session_run_at_end():
#         print('In my_own_session_run_at_end()')
#
#     request.addfinalizer(my_own_session_run_at_end)

