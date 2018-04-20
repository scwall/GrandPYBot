

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ResponseGrandPy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    standard_phrase_response = db.Column(db.String(200), nullable=False)

    def __init__(self, standard_phrase):
        self.standard_phrase_response = standard_phrase


class LoadSiteResponseGrandPy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    load_phrase_response = db.Column(db.String(200), nullable=False)

    def __init__(self, standard_phrase):
        self.load_phrase_response = standard_phrase
