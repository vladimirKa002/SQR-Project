from fastapi.testclient import TestClient
from backend.main import app  # Ensure this import is correct if main.py is where your app is initialized

client = TestClient(app)


def test_get_all_templates():
    response = client.get("/template/all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensuring the response is a list of templates


def test_get_template():
    template_id = 1  # Example ID that should exist
    response = client.get(f"/template/get/{template_id}")
    assert response.status_code == 200
    assert response.json()['id'] == template_id  # Ensure the correct template is fetched


def test_get_template_not_found():
    template_id = 9999  # Non-existing ID
    response = client.get(f"/template/get/{template_id}")
    assert response.status_code == 404


def test_create_template():
    template_data = {"name": "New Template", "picture": b"newpicture", "items": [1, 2]}
    response = client.post("/template/create", json=template_data)
    assert response.status_code == 200
    assert response.json()['name'] == "New Template"


def test_get_item():
    item_id = 1  # Example item ID
    response = client.get(f"/item/get/{item_id}")
    assert response.status_code == 200
    assert response.json()['id'] == item_id


def test_item_not_found():
    item_id = 9999  # This item does not exist
    response = client.get(f"/item/get/{item_id}")
    assert response.status_code == 404
