import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from classic_wow_npcs.api.ping import ping_blueprint
from classic_wow_npcs.api.npcs import npcs_blueprint


# instatiate the db
db = SQLAlchemy()


def create_app(script_info=None):
    """An application factory,
    as explained here: https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/
    """
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    app.register_blueprint(npcs_blueprint)
    app.register_blueprint(ping_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
