# coding: utf-8

import datetime

from flask import request

from app.api import api
from common import render
from common.utils import json_loads
from config import environment
from app.models.log.error import Error


@api.route('/error/index', methods=['GET'])
def error_get():
    for error in Error.objects:
        pass

    return render.ok()


@api.route('/error/create', methods=['POST'])
def error_create():
    data = json_loads(request.data)
    if data is None:
        return render.error('post data error')

    aid = data.get('aid')
    type = data.get('type')
    content = data.get('content')

    type = int(type)
    error = Error(aid=aid, type=type, content=content)
    error.save()

    return render.ok()
