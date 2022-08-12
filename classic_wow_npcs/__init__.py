__version__ = '0.1.0'

import os

from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy


# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)

# instatiate the db
db = SQLAlchemy(app)

class NPC(db.Model):
    __tablename__ = 'npcs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    faction = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    health = db.Column(db.Integer, nullable=False)
    damage = db.Column(db.Integer, nullable=False)
    armor = db.Column(db.Integer, nullable=False)
    background = db.Column(db.text())



class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'ping pong!'
        }


api.add_resource(Ping, '/ping')