
import pytest
import sys
from flask import url_for, json
from parser import Parser
import urllib3
import logging
logging.basicConfig(format='%(message)s')
http = urllib3.PoolManager()


class TestApp:

    def test_page_index(self, client):
        self.r = client.get()
        assert self.r.status == '200 OK'

    def test_parser(self):

        assert Parser.parser("c'est un test") == "un test"

    def test_question(self,client):
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }
        data = {
            'grandfather_question': "raconte moi l'histoire de la rue de liege 20 verviers"
        }
        url = '/question'

        response = client.post(url, data=json.dumps(data), headers=headers)
        assert response.content_type == mimetype
        assert response.json == "raconte l'histoire la rue liege 20 verviers"

