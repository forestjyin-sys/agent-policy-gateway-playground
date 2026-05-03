from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_finance_role_routes_to_finance_model():
    response = client.post(
        "/chat",
        json={
            "userId": "u1",
            "roleId": "finance",
            "message": "hello"
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["allowed"] is True
    assert data["model"] == "gpt-4.1-mini"
    assert data["policy"] == "finance-policy"