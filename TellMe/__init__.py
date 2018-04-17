from . import models
from .views import app

models.db.init_app(app)
