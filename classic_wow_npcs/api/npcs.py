from flask import Blueprint, request
from flask_restx import Resource, Api

from classic_wow_npcs import db
from classic_wow_npcs.api.models import NPC


npcs_blueprint = Blueprint("npcs", __name__)
api = Api(npcs_blueprint)


class NPCsList(Resource):
    def post(self):
        post_data = request.get_json()

        db.session.add(NPC(**post_data))
        db.session.commit()

        response_object = {"message": f'{post_data.get("name")} was added!'}
        return response_object, 201


api.add_resource(NPCsList, "/npcs")
