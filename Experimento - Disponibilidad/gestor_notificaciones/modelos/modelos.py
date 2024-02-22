import enum
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class TipoNotificacion(enum.Enum):
    EVENTOS = 'EVENTOS'
    ENTRENAMINETOS = 'ENTRENAMIENTOS'
    METERIOLOGIA = 'METERIOLOGIA'
    PLANES = 'PLANES'

class Notificacion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tipo_notificacion = db.Column(db.Enum(TipoNotificacion), nullable=False)
    titulo = db.Column(db.String(128), nullable=False)
    descripcion = db.Column(db.String(512), nullable=False)

class NotificacionSchema(SQLAlchemyAutoSchema):
    tipo_notificacion = fields.Enum(TipoNotificacion, by_value=True)
    class Meta:
        model = Notificacion
        load_instance = True