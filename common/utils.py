# coding: utf8

from flask import json


def json_loads(string):
    value = None
    try:
        value = json.loads(string)
    except ValueError, e:
        value = None

    return value
