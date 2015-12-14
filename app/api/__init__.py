# coding: utf8

from flask import Blueprint
from flask.ext.cors import CORS

api = Blueprint('api', __name__)
CORS(api)

from app.api import error

__all__ = [error]
