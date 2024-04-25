from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import logging as log
import json
from pathlib import Path

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)

    app.config['ROOT'] = Path(__file__).parent

    with open(str(app.config['ROOT'] / Path('config.json'))) as conf:
        config = json.load(conf)

        # The webserver secret key.
        app.config['SECRET_KEY'] = config['SECRET_KEY']

        # SQLAlchemy URI defines how to connect to Postgres.
        app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']

    print(app.config['SQLALCHEMY_DATABASE_URI'])

    db.init_app(app=app)
    login_manager.init_app(app=app)

    from website.auth.routes import auth
    app.register_blueprint(auth)

    from website.main.routes import main
    app.register_blueprint(main)

    app.logger.info('Configured App')

    return app
