import requests

base_url = "http://localhost:3030/categories/iddg001"

def test_get_a_category():
    response = requests.get(base_url)
    assert response.status_code == 200
    json_response = response.json()
    print(json_response)
    assert json_response["id"] == "iddg001"