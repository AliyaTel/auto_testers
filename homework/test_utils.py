import pytest
import requests
from utils import get_max, get_min, get_average


def test_get_max():
    assert get_max([1, 5, 3]) == 5
    assert get_max([-10, -3, -20]) == -3

    with pytest.raises(ValueError):
        get_max([])


def test_get_min():
    assert get_min([4, 2, 9]) == 2
    assert get_min([-5, -1, -9]) == -9

    with pytest.raises(ValueError):
        get_min([])


def test_get_average():
    assert get_average([2, 4, 6]) == 4
    assert get_average([1]) == 1
    assert get_average([-3, 3]) == 0

    with pytest.raises(ValueError):
        get_average([])


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



