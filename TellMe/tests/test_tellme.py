from flask import json
from flask import Flask
from TellMe.packages.TellMe import TellMe
from bin.Parser.parser import Parser



class TestApp:

    def test_parser(self):
        parser = Parser('fr')
        assert parser.parser_word("c'est un test") == "test"

    def test_question(self,client):
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }
        data = {
            'grandfather_question': "OpenClassrooms "
        }
        url = '/question'

        response = client.post(url, data=json.dumps(data), headers=headers)
        assert response.content_type == mimetype
        assert response.json['googlemaps_result'] == {'lat': 48.8747578, 'lng': 2.350564700000001}
        assert response.json['wikipedia_result'] == "La rue d’Hauteville est une voie publique située dans le 10e arrondissement de Paris."
        assert response.json['correct_question'] == True
    def test_class_TellMe(self):
        question = "openclassrooms"
        tellme = TellMe("AIzaSyC_0sMqi7mbdoquIuAX8_GpyRuGrNu88qI")
        tellme.set_question(question)
        tellme.google_map()
        tellme.wikipedia()
        assert tellme.get_googlemaps_geocode_result() == {'lat': 48.8747578, 'lng': 2.350564700000001}
        assert tellme.get_wikipedia_result() == 'La rue d’Hauteville est une voie publique située dans le 10e arrondissement de Paris.'

