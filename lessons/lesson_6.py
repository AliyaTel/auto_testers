import requests
import json


def all_posts():
    # response = requests.request('Get', 'https://jsonplaceholder.typicode.com/posts')
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    # print(response.text)
    # print(response.json()[0])
    assert len(response) == 100, 'not all posts'


def new_post():
    body = {
        "title": "lalalala",
        "body": "lala",
        "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
    return response.json()['id']


def delete():
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/42')
    assert response.status_code == 200


def one_post():
    post_id = new_post()
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    print(response)
    assert response['id'] == post_id
    delete()


def post_a_post():
    body = {
        "title": "lalalala",
        "body": "lala",
        "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
    # print(response.status_code)
    assert response.status_code == 201


all_posts()
post_a_post()


def get_coordinates():
    url = 'https://geocoding-api.open-meteo.com/v1/search'
    param = {
        'name': 'Moscow',
        'count': 1
    }
    response = requests.get(url, params=param)
    data = response.json()
    print(data['results'][0]['name'])


get_coordinates()

