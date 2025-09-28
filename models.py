from extensions import db  # usa o mesmo db já criado em extensions.py


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)


class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    psychological = db.Column(db.Text, nullable=False)
    philosophical = db.Column(db.Text, nullable=False)
    religious = db.Column(db.Text, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)

    book = db.relationship("Book", backref=db.backref("characters", lazy=True))


class Agendamento(db.Model):
    __tablename__ = "agendamentos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    data_visita = db.Column(db.DateTime, nullable=False)
    assunto = db.Column(db.String(200), nullable=True)
    criado_em = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
