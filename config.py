
class BaseConfig(object):
    DEBUG = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://@/beehive'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True

    SQLALCHEMY_ECHO = False


class TestingConfig(BaseConfig):
    TESTING = True

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://@/beehive_test'

    SERVER_NAME = 'example.com'
