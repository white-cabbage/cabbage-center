# coding: utf-8

import datetime

from flask import json, request
from app.api import api
from config import environment
from common import render

from config import environment

@api.route('/servers/index', methods=['GET'])
def servers_index():
    db = config.mongo_client['100days']
    users_collection = db['users']

    return render.ok(users_collection.find_one())
