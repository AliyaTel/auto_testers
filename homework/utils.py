import requests
import json
#
# def get_max(numbers):
#     if not numbers:
#         raise ValueError("Список не должен быть пустым")
#     return max(numbers)
#
#
# def get_min(numbers):
#     if not numbers:
#         raise ValueError("Список не должен быть пустым")
#     return min(numbers)
#
#
# def get_average(numbers):
#     if not numbers:
#         raise ValueError("Список не должен быть пустым")
#     return sum(numbers) / len(numbers)
#


# def all_posts():
#     # response = requests.request('Get', 'https://jsonplaceholder.typicode.com/posts')
#     response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
#     # print(response.text)
#     # print(response.json()[0])
#     assert len(response) == 100, 'not all posts'
#
#
# def new_post():
#     body = {
#         "title": 'lalalala',
#         "body": 'lala',
#         "UserID": 1
#     }
#     headers = {'Content-Type': 'application/json'}
#     response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
#     return response.json()['id']
#
# def delete():
#     response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/42')
#     assert response.status_code == 200
#
# def one_post():
#     post_id = new_post()
#     response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
#     print(response)
#     assert response['id'] == post_id
#     delete()
#
# def post_a_post():
#     body = {
#         "title": 'lalalala',
#         "body": 'lalala',
#         "UserID": 1
#     }
#     headers = {'Content-Type': 'application/json'}
#     response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
#     # print(response.status_code)
#     assert response.status_code == 201
#
# all_posts()
# post_a_post()
#
#
# def get_coordinates():
#     url = "https://geocoding-api.open-meteo.com/v1/search"
#     param = {
#         'name': 'New York',
#         "count" : 1
#     }
#     response = requests.get(url, params=param)
#     data = response.json()
#     print(data['results'])
#
# get_coordinates()
#
#
# def get_meteo():
#     url = "https://api.open-meteo.com/v1/forecast"
#     params = {
#         'latitude': 40.71427,
#         'longitude': -74.00597,
#         "current_weather": True
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
#     print(data)
#     print (data ["generationtime_ms"])
#
# get_meteo()
#
#
#


def get_facts():
    url = "https://catfact.ninja/fact"

    fact_1 = requests.get(url).json().get("fact")
    fact_2 = requests.get(url).json().get("fact")
    fact_3 = requests.get(url).json().get("fact")

    facts = {fact_1, fact_2, fact_3}

    print(facts)

get_facts()