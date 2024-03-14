import enum
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///socios.db'  # Usamos SQLite como base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.before_request
def create_tables():
    db.create_all()

class Sexo(enum.Enum):
    MASCULINO = 'MASCULINO'
    FEMENINO = 'FEMENINO'
    OTRO = 'OTRO'

# Definición del modelo de deportistas
class Deportista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(85), nullable=False)
    apellido = db.Column(db.String(22), nullable=False)
    documento = db.Column(db.String(10), unique=True, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    sexo = db.Column(db.Enum(Sexo), nullable=False)
    pais = db.Column(db.String(56), nullable=False)
    estatura = db.Column(db.Float, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    condiciones_medicas = db.Column(db.String(512), nullable=False)

# Definición del esquema de deportistas
class DeportistaSchema(SQLAlchemyAutoSchema):
    sexo = fields.Enum(Sexo, by_value=True)
    class Meta:
        model = Deportista
        load_instance = True

deportista_schema = DeportistaSchema()

# Endpoint para obtener los deportistas que tiene a cargo un socio deportologo
@app.route('/deportistas', methods=['POST'])
def registro_usuario():
    # Validar que el token sea válido para acceder a la información
    token = request.json['token']
    response = requests.post('http://localhost:5000/verify_token', token)
    if response.status_code == 401 or response.status_code == 403:
        return jsonify({'error': 'Unauthorized to access data atheletes'}), 401
    else:
        return [deportista_schema.dump(regla) for regla in Deportista.query.all()], 200

if __name__ == '__main__':
    app.run(debug=True)