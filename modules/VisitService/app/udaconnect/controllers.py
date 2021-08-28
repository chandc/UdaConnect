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
        status = VisitService.create(location)

        return status

