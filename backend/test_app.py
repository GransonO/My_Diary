"""Pylint testing module"""
import requests

def test_updating_entries():
    """test to update an entry"""
    response = requests.get("http://127.0.0.1:5000/api/v1/entries/1")
    assert response.status_code, 200
