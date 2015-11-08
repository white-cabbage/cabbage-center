# coding: utf8

import os


class BaseConfig(object):

    DEBUG = True

    # DB can be erased physically
    DB_ERASABLE = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'development-secret-key')
    MONGODB_SETTINGS = {
        'db': 'cabbage-center-development',
        # 'host': os.environ['MONGO_DB']
        'host': 'localhost',
        'port': 27017
    }


class Production(BaseConfig):

    DEBUG = False

    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGODB_SETTINGS = {
        'db': 'cabbage-center-production',
        'host': os.environ['MONGO_DB']
    }
    DB_ERASABLE = False


class Staging(BaseConfig):

    DB_ERASABLE = False


class Development(BaseConfig):

    pass


class Testing(BaseConfig):

    TESTING = True
    DEBUG = True
