FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copia o restante do projeto
COPY . .

EXPOSE 5000

# usa o objeto "app" do app.py
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
