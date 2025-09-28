# 📚 MVP Backend

Este projeto é um **MVP backend** desenvolvido em **Flask +
SQLAlchemy**, containerizado com **Docker** e conectado a um banco
**PostgreSQL**.\
Ele fornece APIs REST para gerenciar **usuários, livros, personagens e
agendamentos** inspirados nas obras de Dostoiévski.

------------------------------------------------------------------------

## ⚙️ Tecnologias utilizadas

-   Python 3.11\
-   Flask + Flask-SQLAlchemy\
-   PostgreSQL 15 (via Docker)\
-   Gunicorn (produção)\
-   Swagger UI (documentação)\
-   Docker + Docker Compose

------------------------------------------------------------------------

## 📦 Pré-requisitos

-   [Docker](https://docs.docker.com/get-docker/) instalado\
-   [Docker Compose](https://docs.docker.com/compose/)

------------------------------------------------------------------------

## 🚀 Como rodar o projeto

### 1. Clone o repositório

``` bash
git clone <seu-repositorio>
cd Diogo-Narciso-dostoievski-back-and-main
```

### 2. Suba os containers

``` bash
docker compose up -d --build
```

Isso irá subir: - **mvp-db** → PostgreSQL\
- **mvp-backend** → Flask + Gunicorn

### 3. Popule o banco com dados de exemplo

``` bash
docker exec -it mvp-backend python seed.py
```

### 4. Acesse a API

-   Healthcheck: <http://localhost:5000/healthz>\
-   Swagger UI: <http://localhost:5000/swagger>

------------------------------------------------------------------------

## 📖 Endpoints disponíveis

### 🔹 Usuários

-   `GET /api/users/` → Lista todos os usuários\
-   `POST /api/users/` → Cria um novo usuário\

``` json
{
  "name": "Diogo",
  "email": "diogo@example.com",
  "password": "123456"
}
```

------------------------------------------------------------------------

### 🔹 Livros

-   `GET /api/books/` → Lista livros\
-   `POST /api/books/` → Cria livro\

``` json
{
  "title": "Crime e Castigo",
  "description": "Romance psicológico de Dostoiévski"
}
```

------------------------------------------------------------------------

### 🔹 Personagens

-   `GET /api/characters/` → Lista personagens\
-   `POST /api/characters/` → Cria personagem\

``` json
{
  "name": "Raskólnikov",
  "psychological": "Culpa e redenção",
  "philosophical": "Existencialismo",
  "religious": "Busca por absolvição",
  "book_id": 1
}
```

------------------------------------------------------------------------

### 🔹 Agendamentos

-   `GET /api/agendamentos/` → Lista agendamentos\
-   `POST /api/agendamentos/` → Cria agendamento\

``` json
{
  "nome": "Maria",
  "email": "maria@example.com",
  "data_visita": "2025-10-10T14:30:00",
  "assunto": "Discussão literária"
}
```

------------------------------------------------------------------------

## 🛠️ Estrutura do projeto

    📂 Diogo-Narciso-dostoievski-back-and-main
     ┣ 📂 routes/           # Rotas da API (users, books, characters, agendamentos, external)
     ┣ 📜 app.py            # App principal (Factory Pattern)
     ┣ 📜 models.py         # Definição das tabelas do banco
     ┣ 📜 extensions.py     # Extensões (SQLAlchemy)
     ┣ 📜 config.py         # Configurações
     ┣ 📜 seed.py           # Script para popular banco
     ┣ 📜 requirements.txt  # Dependências
     ┣ 📜 Dockerfile        # Imagem backend
     ┣ 📜 docker-compose.yml# Orquestração containers
     ┗ 📂 static/           # swagger.json + assets

------------------------------------------------------------------------

## ✅ Status

-   [x] CRUD Usuários\
-   [x] CRUD Livros\
-   [x] CRUD Personagens\
-   [x] CRUD Agendamentos\
-   [x] Banco populado com dados iniciais\
-   [x] API documentada com Swagger\
-   [x] Infraestrutura Docker pronta

------------------------------------------------------------------------

👉 Pronto para entrega 🎉
