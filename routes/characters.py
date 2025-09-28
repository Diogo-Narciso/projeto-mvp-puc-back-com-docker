from flask import Blueprint, request, jsonify
from models import db, Character

bp = Blueprint("characters", __name__)

# Listar personagens
@bp.route("", methods=["GET"])
@bp.route("/", methods=["GET"])
def listar_personagens():
    chars = Character.query.all()
    return jsonify([
        {
            "id": c.id,
            "name": c.name,
            "psychological": c.psychological,
            "philosophical": c.philosophical,
            "religious": c.religious,
            "book_id": c.book_id
        } for c in chars
    ]), 200

# Criar personagem
@bp.route("", methods=["POST"])
@bp.route("/", methods=["POST"])
def criar_personagem():
    data = request.get_json()
    required = ["name", "psychological", "philosophical", "religious", "book_id"]
    if not data or not all(field in data for field in required):
        return jsonify({"error": "Dados insuficientes"}), 400
    
    char = Character(
        name=data["name"],
        psychological=data["psychological"],
        philosophical=data["philosophical"],
        religious=data["religious"],
        book_id=data["book_id"]
    )
    db.session.add(char)
    db.session.commit()
    return jsonify({"message": "Personagem criado com sucesso", "id": char.id}), 201

# Buscar personagem por ID
@bp.route("/<int:id>", methods=["GET"])
def buscar_personagem(id):
    char = Character.query.get(id)
    if not char:
        return jsonify({"error": "Personagem não encontrado"}), 404
    return jsonify({
        "id": char.id,
        "name": char.name,
        "psychological": char.psychological,
        "philosophical": char.philosophical,
        "religious": char.religious,
        "book_id": char.book_id
    }), 200

# Remover personagem
@bp.route("/<int:id>", methods=["DELETE"])
def deletar_personagem(id):
    char = Character.query.get(id)
    if not char:
        return jsonify({"error": "Personagem não encontrado"}), 404
    db.session.delete(char)
    db.session.commit()
    return jsonify({"message": "Personagem removido com sucesso"}), 200
