from flask import Flask, jsonify, request, render_template
from flask_classful import FlaskView, route

from TellMe.packages.TellMe import TellMe


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    tellme = TellMe("AIzaSyC_0sMqi7mbdoquIuAX8_GpyRuGrNu88qI")

    class MainView(FlaskView):

        @route('/')
        def index(self):
            return render_template('index.html')

        @route('question', methods=["POST"])
        def question(self):
            self.response = dict()
            self.question = request.get_json().get('grandfather_question')
            tellme.set_question(self.question)
            self.question_is_correct = tellme.google_map()
            print(self.question_is_correct)
            if self.question_is_correct is False:
                self.response['correct_question'] = False
            else:
                tellme.wikipedia()
                self.response['correct_question'] = True
                self.response['googlemaps_result'] = tellme.get_googlemaps_geocode_result()
                self.response['wikipedia_result'] = tellme.get_wikipedia_result()
            return jsonify(self.response)

    MainView.register(app, route_base='/')
    return app


app = create_app('config')
if __name__ == '__main__':
    app.run()
