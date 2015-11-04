# coding: utf8

from db import MySQLDB, SqliteDB


class BaseConfig(object):
    DEBUG = True

    # DB can be erased physically
    DB_ERASABLE = False

    # Enable run testing
    ALLOW_TEST = False
    DEFAULT_USER = False


class Production(BaseConfig):
    DEBUG = False

    SECRET_KEY = 'production-secret-key'
    DB = MySQLDB('reformation', host='reformation1.cnisyucjawac.rds.cn-north-1.amazonaws.com.cn',
                 port=3306, user='reformation', passwd='B7rnFfjBeqVR')


class Staging(BaseConfig):

    DB = MySQLDB('reformation_staging', host='172.31.3.226',
                 port=3306, user='reformation', passwd='reformation')

    ALLOW_TEST = True
    DB_ERASABLE = False


class Development(BaseConfig):

    DB = MySQLDB('reformation_development', host='localhost', port=3306, user='reformation', passwd='reformation')
    # DB = SqliteDB('tmp/sqlite_devlopment.db')

    DB_ERASABLE = True


class Testing(BaseConfig):

    DB = SqliteDB('tmp/sqlite_testing.db')
    # DB = MySQLDB('reformation_testing', host='localhost', port=3306, user='reformation', passwd='reformation')

    DB_ERASABLE = True
