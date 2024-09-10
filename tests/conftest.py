import pytest
import requests
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.headers import add_headers
from config import BASE_URL

@pytest.fixture(scope="session")
def session():
    session = requests.Session()
    session.base_url = BASE_URL
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer your_token"
    }
    add_headers(session, headers)
    return session
