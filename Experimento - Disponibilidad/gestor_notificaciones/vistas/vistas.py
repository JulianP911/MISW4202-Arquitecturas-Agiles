import random
import requests
from flask import request
from ..modelos import db, Notificacion, NotificacionSchema
from flask_restful import Resource

regla_schema = NotificacionSchema()

class VistaNotificaciones(Resource):

    def get(self):
        random_decimal_within_range = random.uniform(0, 9)
        if random_decimal_within_range < 2:
            json_payload = {'queue': 'monitor', 'message':  'El servicio de notificaciones no está disponible en este momento. Por favor, inténtelo más tarde.'}
            requests.post('http:localhost:5000/send_message', data=json_payload, headers={'Content-Type': 'application/json'})
            return [], 400
        else:
            json_payload = {'queue': 'monitor', 'message': 'El servicio de notificaciones ha sido consultado.'}
            requests.post('http:localhost:5000/send_message', data=json_payload, headers={'Content-Type': 'application/json'})
            return [regla_schema.dump(regla) for regla in Notificacion.query.all()], 200

    def post(self):
        nueva_notificacion = Notificacion(tipo_notificacion=request.json['tipo_notificacion'], titulo=request.json['titulo'], descripcion=request.json['descripcion'])
        db.session.add(nueva_notificacion)
        db.session.commit()
        return regla_schema.dump(nueva_notificacion)