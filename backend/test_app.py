"""Pylint testing module"""

def test_put_update_data(client):
    """test to update an entry"""
    response = client.get("http://127.0.0.1:5000/api/v1/entries/1")
    assert response.status_code == 200
    assert response[0].id == 1
def test_post_data(client):
    """test add entries"""
    response = client.get("http://127.0.0.1:5000/api/v1/entries")
    assert response.status_code, 200
def test_get_all_entries(client):
    """test to get all entries"""
    response = client.get("http://127.0.0.1:5000/api/v1/entries")
    assert response.status_code, 200
    assert len(response) == 3
def test_get_specific_data(client):
    """test to get specific entries"""
    response = client.get("http://127.0.0.1:5000/api/v1/entries/1")
    assert response.status_code, 200
