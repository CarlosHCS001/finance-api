# Finance API 💰

API REST para gerenciamento de finanças pessoais, desenvolvida com FastAPI e Python.

## 🚀 Tecnologias
- Python 3.13
- FastAPI
- SQLAlchemy
- SQLite
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
# Windows (se uvicorn não for reconhecido no CMD)
venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Acesse: http://localhost:8000/docs

## 📁 Estrutura
O main.py define os endpoints e conecta os outros módulos. O database.py configura a conexão com o SQLite. O models.py define a estrutura da tabela no banco. O schemas.py define e valida os dados que entram e saem pela API.

## 📍 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | / | Status da API |
| GET | /transactions | Busca todas as transações |
| POST | /transactions | Cria uma nova transação |

## 📍 Body (POST /transactions)
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| description | string | ✅ |
| amount | float | ✅ |
| date | date (YYYY-MM-DD) | ✅ |
| category | string | ✅ |

## 📌 Status
🚧 Em desenvolvimento...
