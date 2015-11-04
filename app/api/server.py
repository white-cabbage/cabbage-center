# coding: utf-8

import datetime

from flask import json, request
from app.api import api
from config import environment
from common import render


@api.route('/servers/index', methods=['GET'])
def servers_index():

    return render.ok()
