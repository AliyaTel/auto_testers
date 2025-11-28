import pytest
import requests


@pytest.fixture()
def new_post():
    body = {
        "title": "lalalala",
        "body": "lala",
        "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
    yield response.json()['id']
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/42')


def test_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100, 'not all posts'


@pytest.mark.skip
def test_one_post(new_post):
    post_id = new_post()
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    assert response['id'] == post_id


@pytest.mark.regress
def test_post_a_post():
    body = {
        "title": "lalalala",
        "body": "lala",
        "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
    assert response.status_code == 201
