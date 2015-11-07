# coding: utf8

import datetime

from config import environment

db = environment.db


class Error(db.Document):
    # type
    ERROR = 0
    EXCEPTION = 1

    source = db.StringField(required=True, max_length=200)
    type = db.IntField(required=True)
    content = db.StringField(required=True, max_length=200)

    created_at = db.DateTimeField(default=datetime.datetime.now)
    updated_at = db.DateTimeField(default=datetime.datetime.now)
