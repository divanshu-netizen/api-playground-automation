import requests

base_url = "http://localhost:3030/categories"

def test_retrieve_categories():
    response = requests.get(base_url)
    assert response.status_code == 200

def test_validate_response_body():
    response = requests.get(base_url)
    json_response = response.json()
    print(json_response)
    assert json_response["limit"] == 10
    content_type = response.headers['Content-Type']
    assert content_type == "application/json; charset=utf-8"
