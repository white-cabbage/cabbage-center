# coding: utf-8

import unittest
import requests
import json
import app
import datetime

from app.models.log.error import Error
now = datetime.datetime.now


class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app()
        self.test = self.app.test_client()
        Error.drop_collection()

    def tearDown(self):
        pass

    def test_api_error_create(self):
        res = self.test.post('/api/error/create',
                             data=json.dumps({'aid': '2',
                                              'type': 0,
                                              'content': 'this is a test error'}),
                             content_type='application/json',
                             follow_redirects=True)
        assert res.status_code is 200
    def test_api_error_index(self):
        res = self.test.get('/api/error/index')

if __name__ == '__main__':
    unittest.main()
