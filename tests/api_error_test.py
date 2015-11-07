# coding: utf-8

import unittest
import requests
import json
import app
import datetime

from config import environment

now = datetime.datetime.now


class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app()
        self.app.config.from_object(environment.config)
        self.app.config['TESTING'] = True
        self.test = self.app.test_client()

    def tearDown(self):
        pass

    def test_api_error_create(self):
        res = self.test.post('/api/error/create',
                             data={'aid': '2',
                                   'type': 0,
                                   'content': 'this is a test error'},
                             follow_redirects=True)
        print '\n', res.status_code
        pass

    def test_api_error_index(self):
        res = self.test.get('/api/error/index')
        print '\n', res.data
