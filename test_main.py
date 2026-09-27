from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_invalid_prediction_request():
    response = client.post("/predict", json={})
    assert response.status_code == 422


def test_prediction():
    payload = {
        "tenure_months": 12,
        "support_tickets": 2,
        "monthly_spend_inr": 1000,
        "last_login_days": 5,
        "plan_type": "Basic"
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "churn_probability" in data
    assert "result" in data
