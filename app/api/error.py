# coding: utf-8

import datetime

from flask import json, request

from app.api import api
from common import render
from config import environment
from app.models.log.error import Error


@api.route('/error/create', methods=['GET'])
def servers_index():

    print request.data

    return render.ok()
