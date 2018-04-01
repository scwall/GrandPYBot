from flask import Flask, jsonify, request, render_template, Response, json
from flask_googlemaps import GoogleMaps, Map


def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 37.4419,
                'lng': -122.1419,
                'infobox': "<b>Hello World</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "<b>Hello World from other place</b>"
            }
        ]
    )
    return  sndmap


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    @app.route('/')
    def mapview():
        # creating a map in the view
        mymap = Map(
            identifier="view-side",
            lat=37.4419,
            lng=-122.1419,
            markers=[(37.4419, -122.1419)]
        )
        sndmap = Map(
            identifier="sndmap",
            lat=37.4419,
            lng=-122.1419,
            markers=[
                {
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                    'lat': 37.4419,
                    'lng': -122.1419,
                    'infobox': "<b>Hello World</b>"
                },
                {
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                    'lat': 37.4300,
                    'lng': -122.1400,
                    'infobox': "<b>Hello World from other place</b>"
                }
            ]
        )
        return render_template('example.html', mymap=mymap, sndmap=mapview())
    # def GrandPyBot():
    #     return render_template('test.html', sndmap=mapview())

    @app.route('/add', methods=['POST'])
    def add():
        json = request.get_json()

        return jsonify(json)
    return app
if __name__ == '__main__':
    app = create_app('config')
    GoogleMaps(app)
    app.run()
