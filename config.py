import os
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"
SQLALCHEMY_TRACK_MODIFICATIONS = False
GOOGLEMAPS = "AIzaSyADXfEDu54gj7ROiz-brEVl08RG-pydCkI"
PARSER_LANGUAGE = "fr"
# database initialization
if os.environ.get('DATABASE_URL') is None:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'databases.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
