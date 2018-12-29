from os import getenv

class Config():
    DEBUG = False
    ENV = 'production'

class Development(Config):
    DEBUG = True
    ENV = 'development'

app_config = {
    'development': Development
}