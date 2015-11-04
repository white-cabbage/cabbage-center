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

    @app.before_request
    def _db_connect():
        environment.config.DB.connect()

    @app.teardown_request
    def _db_close(exc):
        if not environment.config.DB.is_closed():
            environment.config.DB.close()

    return app


def init_db(app):
    db = app.config['DB']
    db.connect()

    db.create_tables([], safe=True)

    db.close()


def erase_db(app):

    db = app.config['DB']

    db.drop_tables([], safe=True)

    db.close()


def add_seed():
    pass
