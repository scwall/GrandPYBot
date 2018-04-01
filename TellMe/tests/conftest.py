import pytest
from flask import jsonify, request

from TellMe.views import create_app


@pytest.fixture
def app():
    app = create_app('TellMe.tests.config')
    return app
