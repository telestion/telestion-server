import pytest

from json import dumps


def test_answer_post(client):
    token = None  # TODO: - Test with user
    user_id = 1
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
        'question_id': 1,
        'text': 'Лорем ипсум, много текста, вот и ответ.'
    }
    resp = client.post('/answer', headers=headers, data=dumps(data))
    print(resp.json)

    assert resp.status_code == 201
    assert resp.json['id'] == 1
    assert resp.json['created_by'] == user_id
    assert resp.json['question_id'] == data['question_id']
    assert resp.json['text'] == data['text']


def test_answer_get_no_exc(client):
    resp = client.get('/answer/1')
    print(resp.json)
    assert resp.status_code == 200
    assert resp.json['id'] == 1


# def test_answer_delete_unsuccessful(client):
#     token = None  # TODO: - Test with user
#     headers = {'Authorization': f'Bearer {token}'}
#     resp = client.delete('/answer/1')
#     print(resp.json)
#     assert resp.status_code == 403


def test_answer_delete_successful(client):
    token = None  # TODO: - Test with user
    headers = {'Authorization': f'Bearer {token}'}
    resp = client.delete('/answer/1')
    print(resp.json)
    assert resp.status_code == 200


def test_answer_get_exc(client):
    resp = client.get('/answer/1')
    print(resp.json)
    assert resp.status_code == 404
    assert 'error' in resp.json
