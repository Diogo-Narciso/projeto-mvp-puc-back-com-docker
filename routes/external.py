# routes/external.py
import requests
from flask import Blueprint, request, jsonify

bp = Blueprint("external", __name__)

@bp.get("/autores")
def autores():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify({"error": "Query param 'q' é obrigatório"}), 400
    r = requests.get("https://openlibrary.org/search/authors.json", params={"q": q}, timeout=10)
    return jsonify(r.json()), r.status_code
