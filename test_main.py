from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_name():
    response = client.get("/hello/world")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world"}
