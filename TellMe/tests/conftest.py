import pytest
from flask import jsonify, request

from TellMe.views import create_app


@pytest.fixture
def app():
    app = create_app('TellMe.tests.config')
    print('je modifie la fonction et je renvois')
    return app
@pytest.fixture
def fuction_fix():

    return 'OK 200'