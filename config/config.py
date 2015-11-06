# coding: utf8

import os


class BaseConfig(object):
    DEBUG = True

    # DB can be erased physically
    DB_ERASABLE = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'development-secret-key')
    MONGO_DB = os.environ['MONGO_DB']


class Production(BaseConfig):
    DEBUG = False

    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGO_DB = os.environ['MONGO_DB']
    DB_ERASABLE = False


class Staging(BaseConfig):

    DB_ERASABLE = False


class Development(BaseConfig):

    pass


class Testing(BaseConfig):

    pass
