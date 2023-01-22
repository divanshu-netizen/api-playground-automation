import requests

base_url = "http://localhost:3030/categories/iddg001"

def test_remove_category():
    response = requests.delete(base_url)
    assert response.status_code == 200
