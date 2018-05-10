import os
import pytest
import googlemaps
import pytest
import requests
from _pytest.monkeypatch import MonkeyPatch

from TellMe import models
from TellMe.views import create_app
"""
Patch requests and googlemaps functions to return a value even 
if there is no connection to the external service
"""
@pytest.fixture(scope='session')
def monkeypatch_session():
    m = MonkeyPatch()
    yield m
    m.undo()

@pytest.fixture(scope="session")
def app(monkeypatch_session,request):
    def teardown():
        TESTDB_PATH = app.config['SQLALCHEMY_DATABASE_URI'].replace("sqlite:///","")
        models.db.drop_all()
        if os.path.exists(TESTDB_PATH):
            os.unlink(TESTDB_PATH)



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


    monkeypatch_session.setattr(googlemaps, 'Client', googlemaps_return)
    monkeypatch_session.setattr(requests, 'get', requests_return)
    app = create_app('TellMe.tests.config')
    app.app_context().push()
    models.db.create_all()
    models.db.session.add(
        models.ResponseGrandPy(
            "testing response"))
    models.db.session.add(models.LoadSiteResponseGrandPy("testing loadsite"))
    models.db.session.add(models.ResponseGrandPyError("testing error"))
    models.db.session.commit()
    request.addfinalizer(teardown)
    return app

