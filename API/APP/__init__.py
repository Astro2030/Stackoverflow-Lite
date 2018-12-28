import os

from flask import Flask
from stack.app.v1.views.blog import BP 
from stack.app.v1.views import blog
from stack.instance.config import app_config


def create_app(config_name='development'):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(blog.BP)
    app.config.from_object(app_config[config_name])
    return app
