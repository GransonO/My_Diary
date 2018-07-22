# conftest.py
"""Pytest fixtures"""
import pytest

# pylint: disable=W0621
from app import create_app

@pytest.fixture
def app():
    """Creates an 'app' fixture for endpoints testing"""
    app = create_app()
    app.debug = True
    return app
