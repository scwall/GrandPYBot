from flask import Flask, jsonify, request, render_template
from TellMe.packages.questionSearch import QuestionSearch
from TellMe import models
import logging as lg
import random


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    models.db.init_app(app)
    tellme = QuestionSearch(app.config['GOOGLEMAPS'],app.config['PARSER_LANGUAGE'])
    @app.cli.command()
    def init_db():
        models.db.drop_all()
        models.db.create_all()
        models.db.session.add(
            models.ResponseGrandPy(
                "Huh, je vais te raconter une histoire sur cette endroit "))
        models.db.session.add(models.ResponseGrandPy(
            "Je vais te compter une histoire de mon souvenir "))
        models.db.session.add(models.LoadSiteResponseGrandPy("Pose moi une question"))
        models.db.session.add(models.LoadSiteResponseGrandPy("Je suis à ton écoute"))
        models.db.session.add(models.ResponseGrandPyError("PARLE PLUS FORT ! Je n'ai pas compris la question "))
        models.db.session.commit()
        lg.warning('Database initialized!')

    @app.route('/')
    def index():
        return render_template('index.html')

    # Link for receiving the ajax answer to the question to grand py bot
    @app.route('/question', methods=["POST"])
    def question():
        response = dict()
        question = request.get_json().get('grandfather_question')
        tellme.set_question(question)
        question_is_correct = tellme.google_map()
        if question_is_correct is False:
            response['correct_question'] = False
        else:
            tellme.wikipedia()
            response['correct_question'] = True
            response['googlemaps_result'] = tellme.get_googlemaps_geocode_result()
            response['wikipedia_result'] = tellme.get_wikipedia_result()
        return jsonify(response)

    #When loading the site references the database with custom phrases
    @app.route('/loadsite', methods=["POST"])
    def loadsite():
        load_site = object()
        random_response = object()
        random_error = object()
        response = request.get_json().get('loadsite')
        if response == 'start':
            load_site = models.LoadSiteResponseGrandPy.query.filter_by(
                id=random.randrange(1, (models.LoadSiteResponseGrandPy.query.count() + 1))).first()
            random_response = models.ResponseGrandPy.query.filter_by(
                id=random.randrange(1, (models.ResponseGrandPy.query.count() + 1))).first()
            random_error = models.ResponseGrandPyError.query.filter_by(
                id=random.randrange(1, (models.ResponseGrandPyError.query.count() + 1))).first()
        return jsonify(
            {'randomHello': load_site.load_phrase_response, 'randomResponse': random_response.standard_phrase_response,
             'randomError': random_error.standard_phrase_response_error})

    return app


app = create_app('config')
app.app_context().push()

if __name__ == '__main__':
    app.run()
