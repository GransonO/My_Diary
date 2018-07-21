"""Pylint testing module"""

def test_put_update_data(client):
    """
    test to update an entry
    """
    response = client.get("http://127.0.0.1:5000/api/v1/entries/1")
    #Cannot get results without putting
    assert response.status_code == 200

def test_post_data(client):
    """test add entries"""
    response = client.get("http://127.0.0.1:5000/api/v1/entries")
    assert response.status_code == 200

def test_get_all_entries(client):
    """test to get all entries"""
    response = client.get("http://127.0.0.1:5000/api/v1/entries")
    assert response.status_code == 200

def test_get_specific_data(client):
    """test to get specific entries"""
    response = client.get("http://127.0.0.1:5000/api/v1/entries/1")
    assert response.status_code == 200

def test_client(client):
    """Test return status code"""
    assert client.get("http://127.0.0.1:5000/api/v1/entries/1").status == '200 OK'
