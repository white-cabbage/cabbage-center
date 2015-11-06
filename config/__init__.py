# -*- coding: utf-8 -*-

import os
# import argparse
from config import Production, Staging, Development, Testing
from db import MongoDB


try:
    env = os.environ['FLASK_ENV']
except KeyError as e:
    raise Exception('Please set the environment key FLASK_ENV to Production/Staging/Development/Testing')


class Environment(object):

    def __init__(self):

        global env
        if env not in ('Production', 'Staging', 'Development', 'Testing'):
            print 'Invalid environment key, defaulting to Development'
            env = 'Development'

        if env == 'Production':
            self.config = Production()
        elif env == 'Staging':
            self.config = Staging()
        elif env == 'Testing':
            self.config = Testing()
        else:
            self.config = Development()

        self.mongo_client = MongoDB(self.config.MONGO_DB)

environment = Environment()
