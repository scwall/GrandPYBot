import logging as lg

from flask_sqlalchemy import SQLAlchemy

from TellMe.views import app

db = SQLAlchemy()


class ResponseGrandPy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    standard_phrase = db.Column(db.String(200), nullable=False)

    def __init__(self, standard_phrase):
        self.standard_phrase = standard_phrase


@app.cli.command()
def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(ResponseGrandPy("PARLE PLUS FORT ! Je n'ai pas compris la question "))
    db.session.add(ResponseGrandPy("huh, je vais te raconter une histoire à propos de cette endroit "))
    db.session.commit()
    lg.warning('Database initialized!')
