# coding: utf-8

import datetime

from flask import json, request

from app.api import api
from common import render
from config import environment
from app.models.log.error import Error


@api.route('/error/index', methods=['GET'])
def error_get():
    for error in Error.objects:
        pass

    return render.ok()


@api.route('/error/create', methods=['POST'])
def error_create():
    # data = json.loads(request.data)
    print '\n', 'request.data: ', request.data
    return render.ok()

    aid = data.get('aid')
    type = data.get('type')
    content = data.get('content')

    type = int(type)
    error = Error(aid=aid, type=type, content=content)
    error.save()

    return render.ok()
