from flask import json
from TellMe.packages.questionSearch import QuestionSearch
from TellMe.packages.parser import Parser


class TestApp:
    #
    # def test_parser(self):
    #     parser = Parser('fr')
    #     assert parser.parser_word("c'est un test") == "test"

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
        assert response.json['googlemaps_result'] == {'lat': 0.00, 'lng': 0.00}
        assert response.json['wikipedia_result'] == True
        assert response.json['correct_question'] == True

    # def test_loadsite(self,client):
    #     mimetype = 'application/json'
    #     headers = {
    #         'Content-Type': mimetype,
    #         'Accept': mimetype
    #     }
    #     data = {
    #         'loadsite': 'start'
    #     }
    #     url = '/loadsite'
    #
    #     response = client.post(url, data=json.dumps(data), headers=headers)
    #     assert response.content_type == mimetype
    #     assert response.json['randomHello'] == ""


    def test_class_TellMe(self):
        question = "openclassrooms"
        tellme = QuestionSearch("AIzaSyC_0sMqi7mbdoquIuAX8_GpyRuGrNu88qI")
        tellme.set_question(question)
        tellme.google_map()
        tellme.wikipedia()
        assert tellme.get_googlemaps_geocode_result() == {'lat': 0.00, 'lng': 0.00}
        assert tellme.get_wikipedia_result() == True

