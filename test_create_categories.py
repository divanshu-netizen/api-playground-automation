import requests
import json

base_url = "http://localhost:3030/categories"

def test_create_categories():
    response = requests.post(url=base_url, json=json.loads('{"name": "string","id": "iddg001"}'))
    print(response.status_code)
    print(response)
    json_response = response.json()
    assert response.status_code == 201
