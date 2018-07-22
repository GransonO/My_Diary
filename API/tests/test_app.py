"""Pylint testing module"""
import pytest

def test_incomplete(client):
    """ test incomplete request """
    response = client.get("http://127.0.0.1:5000/api/v1/entries/")
    assert response.status_code == 404

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

def test_get_return_title(client):
    """test to get specific title returned """
    response = client.get("http://127.0.0.1:5000/api/v1/entries/1")
    assert response.json['title'] == 'That day I Laughed'

def test_get_return_date(client):
    """test to get specific title returned """
    response = client.get("http://127.0.0.1:5000/api/v1/entries/1")
    assert response.json['date'] == '02-07-2018'

def test_for_api_mimetypes(client):
    """test request return object """
    response = client.get("http://127.0.0.1:5000/api/v1/entries/1")
    assert response.mimetype == 'application/json'

@pytest.mark.options(debug=False)
def test_app_debug_state(app):
    """Assert that app is not in debug mode"""
    assert not app.debug, 'true'
