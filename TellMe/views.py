import sys
from flask import Flask, jsonify, request, render_template, Response, json
from flask_googlemaps import GoogleMaps, Map
from flask_classful import FlaskView, route
from parser import Parser
def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    class MainView(FlaskView):
        @route('/')
        def index(self):
            return render_template('index.html')

        @route('question', methods=["POST"])
        def question(self):
            self.question = request.get_json().get('grandfather_question')
            self.question = Parser.parser(self.question)
            return jsonify(self.question)

    MainView.register(app, route_base='/')
    return app


if __name__ == '__main__':
    app = create_app('config')
    GoogleMaps(app)
    app.run()
