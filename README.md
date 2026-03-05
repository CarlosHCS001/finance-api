# Finance API 💰

API REST para gerenciamento de finanças pessoais, desenvolvida com FastAPI e Python.

## 🚀 Tecnologias
- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn

## ⚙️ Como rodar localmente

### Pré-requisitos
- Python 3.10+
- Git

### Instalação
```bash
# Clone o repositório
git clone https://github.com/CarlosHCS001/finance-api.git
cd finance-api

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode a API
uvicorn app.main:app --reload
```

Acesse: http://localhost:8000/docs

## 📍 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | / | Status da API |

## 📌 Status
🚧 Em desenvolvimento...