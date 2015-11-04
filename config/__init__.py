# -*- coding: utf-8 -*-

import os
# import argparse
from config import Production, Staging, Development, Testing

try:
    env = os.environ['FLASK_ENV']
except KeyError as e:
    print 'error'
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

environment = Environment()
