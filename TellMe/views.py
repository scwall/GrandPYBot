from flask import Flask, jsonify, request, render_template
from TellMe.packages.TellMe import TellMe
from TellMe import models
import logging as lg
import random

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    models.db.init_app(app)
    return app


tellme = TellMe("AIzaSyC_0sMqi7mbdoquIuAX8_GpyRuGrNu88qI")
app = create_app('config')
app.app_context().push()


@app.cli.command()
def init_db():
    models.db.drop_all()
    models.db.create_all()
    models.db.session.add(models.ResponseGrandPy("PARLE PLUS FORT ! Je n'ai pas compris la question "))
    models.db.session.add(models.ResponseGrandPy("huh, je vais te raconter une histoire à propos de cette endroit "))
    models.db.session.add(models.LoadSiteResponseGrandPy("MMMM bienvenue chère utilisateur, pose moi une question"))
    models.db.session.commit()
    lg.warning('Database initialized!')


@app.route('/')
def index():
    loadsite = models.LoadSiteResponseGrandPy.query.filter_by(id=random.randrange(1, 4)).first()

    return render_template('index.html', loadsite=loadsite.load_phrase_response)


@app.route('/question', methods=["POST"])
def question():
    response = dict()
    question = request.get_json().get('grandfather_question')
    tellme.set_question(question)
    question_is_correct = tellme.google_map()
    print(question_is_correct)
    if question_is_correct is False:
        response['correct_question'] = False
    else:
        tellme.wikipedia()
        response['correct_question'] = True
        response['googlemaps_result'] = tellme.get_googlemaps_geocode_result()
        response['wikipedia_result'] = tellme.get_wikipedia_result()
    return jsonify(response)


if __name__ == '__main__':
    app.run()
