from flask import Blueprint, request, jsonify
from models import db, Book

bp = Blueprint("books", __name__)

# Listar livros
@bp.route("", methods=["GET"])
@bp.route("/", methods=["GET"])
def listar_livros():
    books = Book.query.all()
    return jsonify([{"id": b.id, "title": b.title, "description": b.description} for b in books]), 200

# Criar livro
@bp.route("", methods=["POST"])
@bp.route("/", methods=["POST"])
def criar_livro():
    data = request.get_json()
    if not data or not data.get("title") or not data.get("description"):
        return jsonify({"error": "Dados insuficientes"}), 400
    
    book = Book(title=data["title"], description=data["description"])
    db.session.add(book)
    db.session.commit()
    return jsonify({"message": "Livro criado com sucesso", "id": book.id}), 201

# Buscar livro por ID
@bp.route("/<int:id>", methods=["GET"])
def buscar_livro(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"error": "Livro não encontrado"}), 404
    return jsonify({"id": book.id, "title": book.title, "description": book.description}), 200

# Remover livro
@bp.route("/<int:id>", methods=["DELETE"])
def deletar_livro(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"error": "Livro não encontrado"}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Livro removido com sucesso"}), 200
