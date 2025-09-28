from flask import Flask, render_template, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from config import Config
from extensions import db
from routes.books import bp as books_bp
from routes.characters import bp as chars_bp
from routes.agendamentos import bp as ag_bp
from routes.users import bp as users_bp
from routes.external import bp as external_bp


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(Config)
    db.init_app(app)

    # Swagger
    SWAGGER_URL = "/swagger"
    API_URL = "/static/swagger.json"
    swaggerui = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
    app.register_blueprint(swaggerui, url_prefix=SWAGGER_URL)

    # Registrar Blueprints
    app.register_blueprint(users_bp, url_prefix="/api/users")
    app.register_blueprint(books_bp, url_prefix="/api/books")
    app.register_blueprint(chars_bp, url_prefix="/api/characters")
    app.register_blueprint(ag_bp, url_prefix="/api/agendamentos")
    app.register_blueprint(external_bp, url_prefix="/api")

    # Rota principal
    @app.route("/")
    def index():
        return render_template("index.html")

    # Healthcheck
    @app.route("/healthz")
    def health():
        return jsonify({"status": "ok"}), 200

    return app


# Instância global para o Gunicorn
app = create_app()

# Executa apenas em modo local (python app.py)
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)
