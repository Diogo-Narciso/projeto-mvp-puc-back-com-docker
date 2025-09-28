# routes/agendamentos.py
from datetime import datetime
from flask import Blueprint, request, jsonify
from extensions import db
from models import Agendamento

bp = Blueprint("agendamentos", __name__)

@bp.get("/")
def listar():
    items = Agendamento.query.order_by(Agendamento.criado_em.desc()).all()
    return jsonify([
        {
            "id": i.id,
            "nome": i.nome,
            "email": i.email,
            "data_visita": i.data_visita.isoformat(),
            "assunto": i.assunto,
            "criado_em": i.criado_em.isoformat()
        } for i in items
    ]), 200

@bp.post("/")
def criar():
    data = request.get_json() or {}
    try:
        nome = data["nome"].strip()
        email = data["email"].strip()
        data_visita = datetime.fromisoformat(data["data_visita"])
        assunto = data.get("assunto")
    except Exception:
        return jsonify({"error": "Payload inválido"}), 400

    ag = Agendamento(nome=nome, email=email, data_visita=data_visita, assunto=assunto)
    db.session.add(ag)
    db.session.commit()
    return jsonify({"message": "Agendamento criado", "id": ag.id}), 201

@bp.put("/<int:ag_id>")
def atualizar(ag_id: int):
    ag = Agendamento.query.get(ag_id)
    if not ag:
        return jsonify({"error": "Agendamento não encontrado"}), 404

    data = request.get_json() or {}
    if "nome" in data: ag.nome = data["nome"]
    if "email" in data: ag.email = data["email"]
    if "data_visita" in data:
        ag.data_visita = datetime.fromisoformat(data["data_visita"])
    if "assunto" in data: ag.assunto = data["assunto"]

    db.session.commit()
    return jsonify({"message": "Agendamento atualizado"}), 200

@bp.delete("/<int:ag_id>")
def remover(ag_id: int):
    ag = Agendamento.query.get(ag_id)
    if not ag:
        return jsonify({"error": "Agendamento não encontrado"}), 404
    db.session.delete(ag)
    db.session.commit()
    return jsonify({"message": "Agendamento removido"}), 200
