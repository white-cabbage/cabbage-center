# coding: utf8

import os

from flask import Flask, Response

from app.api import api
from config import environment


__version__ = "0.0.1"
__description__ = "Cabbage Project Center"


def create_app():
    app = Flask(__name__)

    app.config.from_object(environment.config)
    app.register_blueprint(api, url_prefix='/api')

    # Init db with MongoEngine
    environment.db.init_app(app)

    @app.before_request
    def _db_connect():
        pass

    @app.teardown_request
    def _db_close(exc):
        pass

    return app


def init_db(app):

    pass


def erase_db(app):

    pass


def add_seed():
    pass
