from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_formats_known_input():
    response = client.get("/formats/pdf")
    assert response.status_code == 200
    assert "outputs" in response.json()


def test_formats_unknown_input():
    response = client.get("/formats/unknownformat")
    assert response.status_code == 200
    assert response.json()["outputs"] == []
