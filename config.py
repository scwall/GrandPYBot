import os
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
TESTING = True
# database initialization
if os.environ.get('DATABASE_URL') is None:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test_databases.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
