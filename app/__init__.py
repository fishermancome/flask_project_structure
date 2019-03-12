from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


from config import config


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app


from app.main.models import base
