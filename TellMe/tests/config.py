import os
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test_databases.db')
DEBUG = True
TESTING = True
LIVESERVER_PORT = 5001
SQLALCHEMY_TRACK_MODIFICATIONS = False
GOOGLEMAPS = "AIzaSyADXfEDu54gj7ROiz-brEVl08RG-pydCkI"
PARSER_LANGUAGE = "fr"