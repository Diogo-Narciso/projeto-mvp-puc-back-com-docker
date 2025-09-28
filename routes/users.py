from flask import Blueprint, request, jsonify
from extensions import db
from models import User

bp = Blueprint("users", __name__)

@bp.post("/")
def criar_usuario():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Dados insuficientes"}), 400

    try:
        user = User(name=data["name"], email=data["email"], password="123456")
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuário cadastrado", "id": user.id}), 201
    except Exception as e:
        return jsonify({"error": f"Erro ao cadastrar usuário: {str(e)}"}), 500

@bp.get("/")
def listar_usuarios():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users]), 200

@bp.delete("/<int:user_id>")
def deletar_usuario(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuário deletado com sucesso"}), 200
