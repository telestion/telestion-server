import os

from flask import Flask, g
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    api = Api(app)

    from server.api.v1 import Answer

    """
    Answer URL.

    Allowed methods:
    - GET (Returns answer with specified id)
    - POST (Posts a new answer)
    """
    api.add_resource(Answer, '/answer', '/answer/<int:id>')

    return app
