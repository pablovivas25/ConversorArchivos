from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_convert_without_file_fails():
    response = client.post(
        "/convert",
        data={"target_format": "pdf"}
    )
    assert response.status_code == 422
