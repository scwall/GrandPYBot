# test_app.py
import pytest
import sys
from flask import url_for, json
from ..views import result_google_maps
import urllib3
import logging
logging.basicConfig(format='%(message)s')
http = urllib3.PoolManager()


class TestApp:

    def test_connection(self, client):
        self.r = client.get()
        assert self.r.status == '200 OK'

    def test_jquery(self,client):
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }
        data = {
            'grandfather_question': 'question'
        }
        url = '/add'

        response = client.post(url, data=json.dumps(data), headers=headers)
        assert response.content_type == mimetype
        assert response.json == {'grandfather_question': 'question'}
    def test_result_google_maps(self):
        result_google_maps('')

