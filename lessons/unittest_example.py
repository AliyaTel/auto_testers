import unittest
import requests


class TestPostApi(unittest.TestCase):
    def setUp(self) -> None:
        body = {
            "title": "lalalala",
            "body": "lala",
            "userId": 1
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
        self.post_id = response.json()['id']

    def tearDown(self) -> None:
        response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/42')
        assert response.status_code == 200

    def test_all_posts(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
        self.assertEqual(len(response), 100)

    def test_post_a_post(self):
        body = {
            "title": "lalalala",
            "body": "lala",
            "userId": 1
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_one_post(self):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}').json()
        print(response)
        self.assertEqual(response['id'], self.post_id)
