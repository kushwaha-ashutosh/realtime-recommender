from fastapi.testclient import TestClient
from services.model_service.app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_recommendations():
    response = client.get("/recommendations?user_id=1")
    assert response.status_code == 200

    data = response.json()
    assert "recommendations" in data
    assert len(data["recommendations"]) > 0
