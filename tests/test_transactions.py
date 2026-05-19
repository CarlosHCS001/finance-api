from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_transaction_auto_category():
    response = client.post("/transactions", json={
        "description": "Comprei no mercado hoje",
        "amount": 150.50,
        "date": "2025-03-13"
    })
    assert response.status_code == 200
    assert response.json()["category"] == "alimentação"

def test_get_transactions():
    response = client.get("/transactions")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_transactions_summary():
    response = client.get("/transactions/summary")
    assert response.status_code == 200
    assert "total" in response.json()
    assert "by_category" in response.json()
