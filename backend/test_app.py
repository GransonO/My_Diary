"""Pylint testing module"""
import requests

def test_response():
    """test to get all entries"""
    response = requests.get("http://127.0.0.1:5000/api/v1")
    assert response.status_code, 200
