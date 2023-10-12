from decouple import config


class Config():
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}