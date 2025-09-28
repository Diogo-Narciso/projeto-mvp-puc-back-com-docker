from app import create_app
from extensions import db
from models import User, Book, Character, Agendamento
from datetime import datetime, timedelta

# Cria a aplicação e inicializa o contexto
app = create_app()

with app.app_context():
    print("🔄 Criando tabelas (se não existirem)...")
    db.create_all()

    # Usuários
    if not db.session.query(User).first():
        user1 = User(name="Diogo", email="diogo@example.com", password="123456")
        user2 = User(name="Maria", email="maria@example.com", password="123456")
        db.session.add_all([user1, user2])

    # Livros
    if not db.session.query(Book).first():
        book1 = Book(title="Crime e Castigo", description="Romance psicológico de Dostoiévski")
        book2 = Book(title="Os Irmãos Karamázov", description="Explora questões filosóficas e religiosas")
        db.session.add_all([book1, book2])

        # Personagens
        char1 = Character(
            name="Raskólnikov",
            psychological="Culpa e redenção",
            philosophical="Existencialismo",
            religious="Busca por absolvição",
            book=book1
        )
        char2 = Character(
            name="Ivan Karamázov",
            psychological="Dúvida e razão",
            philosophical="Ateísmo e livre-arbítrio",
            religious="Conflito espiritual",
            book=book2
        )
        db.session.add_all([char1, char2])

    # Agendamentos
    if not db.session.query(Agendamento).first():
        ag1 = Agendamento(
            nome="João Silva",
            email="joao@example.com",
            data_visita=datetime.now() + timedelta(days=3),
            assunto="Visita à biblioteca"
        )
        ag2 = Agendamento(
            nome="Ana Souza",
            email="ana@example.com",
            data_visita=datetime.now() + timedelta(days=5),
            assunto="Reunião sobre Dostoiévski"
        )
        db.session.add_all([ag1, ag2])

    db.session.commit()
    print("✅ Banco populado com dados de exemplo!")
