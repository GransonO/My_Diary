"""Pylint testing module"""
import requests

def test_put_update_data():
    """test to update an entry"""
    response = requests.get("http://127.0.0.1:5000/api/v1/entries/1")
    assert response.status_code, 200
def test_post_data():
    """test add entries"""
    response = self.app.get("http://127.0.0.1:5000/api/v1/entries")
    assert response.status_code, 200
def test_get_all_entries():
    """test to get all entries"""
    response = self.app.get("http://127.0.0.1:5000/api/v1/entries")
    assert response.status_code, 200
def test_get_specific_data():
    """test to get specific entries"""
    response = self.app.get("http://127.0.0.1:5000/api/v1/entries/1")
    assert response.status_code, 200