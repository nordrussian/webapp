from webapp.db import db
from flask import Flask
# from flask_migrate import Migrate
from webapp.lector.views import blueprint as lector_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    # migrate = Migrate(app, db)
    app.register_blueprint(lector_blueprint)

    return app

   