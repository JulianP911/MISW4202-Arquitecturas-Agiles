from gestor_notificaciones import create_app
from .modelos import db, Notificacion
from flask_restful import Api
from .vistas import VistaNotificaciones

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaNotificaciones, '/notificaciones')