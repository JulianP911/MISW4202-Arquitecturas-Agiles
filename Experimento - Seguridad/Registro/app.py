from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import hashlib
import bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///users.db"  # Usamos SQLite como base de datos
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.before_request
def create_tables():
    db.create_all()


# Definición del modelo de usuario
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


# Endpoint para registrar un usuario
@app.route("/registro", methods=["POST"])
def registro_usuario():
    data = request.json
    if "username" not in data or "password" not in data:
        return jsonify({"error": "Se requiere nombre de usuario y contraseña"}), 400

    nuevo_usuario = User(username=data["username"], password=data["password"])

    try:
        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify({"mensaje": "Usuario registrado correctamente"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Nombre de usuario ya existente"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Endpoint para autenticar un usuario
@app.route("/autenticacion", methods=["POST"])
def autenticar_usuario():
    data = request.json
    if "username" not in data or "password" not in data:
        return jsonify({"error": "Se requiere nombre de usuario y contraseña"}), 400

    usuario = User.query.filter_by(username=data["username"]).first()
    if usuario and usuario.password == data["password"]:
        return jsonify({"autenticado": True}), 200
    else:
        return jsonify({"autenticado": False}), 401


@app.route("/hash_contraseña", methods=["GET"])
def hash_contraseña():
    username = request.args.get("username")

    if not username:
        return jsonify({"error": "Se requiere nombre de usuario"}), 400

    usuario = User.query.filter_by(username=username).first()
    if usuario:
        hash_password = bcrypt.hashpw(usuario.password.encode(), salt=bcrypt.gensalt())
        return jsonify({"hash_contraseña": bytes.decode(hash_password)}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=8080)
