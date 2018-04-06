from flask import json

from TellMe.packages.TellMe import TellMe
from bin.Parser.parser import Parser
import urllib3
import logging
logging.basicConfig(format='%(message)s')
http = urllib3.PoolManager()

def fuction(numb1,numb2):
    return numb1 * numb2

class TestApp:

    def test_page_index(self, client):
        self.r = client.get()
        assert self.r.status == '200 OK'

    def test_parser(self):
        parser = Parser('fr')
        assert parser.parser_word("c'est un test") == "un test"

    def test_question(self,client):
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }
        data = {
            'grandfather_question': "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        }
        url = '/question'

        response = client.post(url, data=json.dumps(data), headers=headers)
        assert response.content_type == mimetype
        assert response.json['googlemaps'] == ""
        assert response.json['history'] == ""
    def test_class_TellMe(self):
        question = "Salut GrandPy ! Est-ce que tu connais l'adresse  d'openclassrooms"
        tellme = TellMe("AIzaSyC_0sMqi7mbdoquIuAX8_GpyRuGrNu88qI")
        tellme.set_question(question)
        assert tellme.google_map() == {}
        assert tellme.wikipedia() == str()

