import socket
import json
from flask import request
from flask_restx import Namespace, Resource 
from app.udaconnect.services import VisitService


api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa

@api.route("/visits")
class ServiceResource(Resource):   
    def post(self):
        location = request.get_json()
    # location['creation_time'] created by the database
        json.dumps({"successfully read input: ":location})
        status = VisitService.create(location)

        return status

