import pytest
from server import app

client = app.test_client()


def test_dummy():
    resp = client.get('/dummy')
    print(resp.json)
    assert resp.status_code == 200
    assert 'message' in resp.json
    assert resp.json['message'] == 'Hello world!'
