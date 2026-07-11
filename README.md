# Finance API 💰

## 🎯 O Problema
A gestão financeira pessoal muitas vezes falha pela falta de padronização e dificuldade em visualizar gastos por categoria. Planilhas manuais são propensas a erros e não oferecem uma interface programável para automações futuras.

## 🚀 A Solução
Uma API REST robusta desenvolvida para ser o motor de um sistema de finanças pessoais. Focada em **consistência de dados**, **categorização automática** e pronta para escala (preparada para migração de SQLite para PostgreSQL).

## 🛠️ Tecnologias e Decisões Técnicas
- **Python 3.13**: Versão mais recente para aproveitar melhorias de performance.
- **FastAPI**: Escolhido pela alta performance e validação nativa com Pydantic.
- **SQLAlchemy 2.0**: Uso de ORM para abstração do banco de dados e facilitar a troca para PostgreSQL.
- **Pydantic**: Garantia de que nenhum dado inválido entre no banco.
- **GitHub Actions**: Pipeline de CI configurado para garantir que novos códigos não quebrem o sistema.

## 🏗️ Estrutura do Projeto
- `/app`: Núcleo da aplicação (Models, Services, Endpoints).
- `/tests`: Garantia de qualidade e funcionamento das regras de negócio.
- `.env`: Gestão de variáveis de ambiente para segurança de credenciais.

## 🏁 Como Executar
1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv .venv`
3. Instale as dependências: `pip install -r requirements.txt`
4. Inicie o servidor: `uvicorn app.main:app --reload`