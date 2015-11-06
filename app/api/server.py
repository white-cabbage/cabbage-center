# coding: utf-8

import datetime

from flask import json, request
from app.api import api
from common import render

from config import environment

@api.route('/servers/index', methods=['GET'])
def servers_index():
    db = environment.mongo_client['100days']
    users_collection = db['users']
    one = users_collection.find_one()

    return render.ok(one)
