import json
import os
import sys

# Ensure the directory containing app.py is on sys.path
CURRENT_DIR = os.path.dirname(__file__)
APP_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)

from app import create_app


def get_client():
    return create_app().test_client()


def test_home():
    client = get_client()
    resp = client.get('/')
    assert resp.status_code == 200
    body = resp.get_json()
    assert body == {"message": "Welcome to the Flask App"}


def test_health():
    client = get_client()
    resp = client.get('/health')
    assert resp.status_code == 200
    body = resp.get_json()
    assert body == {"status": "ok"}


def test_post_data_success():
    client = get_client()
    payload = {"name": "Fatima", "value": 42}
    resp = client.post('/data', data=json.dumps(payload), content_type='application/json')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["received"]["name"] == "Fatima"
    assert data["count"] == len(payload)


def test_post_data_bad():
    client = get_client()
    resp = client.post('/data', data="notjson", content_type='application/json')
    assert resp.status_code == 400
