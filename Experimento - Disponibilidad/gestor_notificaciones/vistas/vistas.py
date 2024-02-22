from flask import request
from ..modelos import db, Notificacion, NotificacionSchema
from flask_restful import Resource

regla_schema = NotificacionSchema()

class VistaNotificaciones(Resource):

    def get(self):
        return [regla_schema.dump(regla) for regla in Notificacion.query.all()]

    def post(self):
        nueva_notificacion = Notificacion(tipo_notificacion=request.json['tipo_notificacion'], titulo=request.json['titulo'], descripcion=request.json['descripcion'])
        db.session.add(nueva_notificacion)
        db.session.commit()
        return regla_schema.dump(nueva_notificacion)