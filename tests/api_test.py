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
        self.test = self.app.test_client()

    def tearDown(self):
        pass

    def test_api_error(self):
        res = self.test.get('/api/error/create')
        print res.data

if __name__ == '__main__':
    unittest.main()
