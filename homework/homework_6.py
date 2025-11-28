import requests
import json


def all_posts():
    response = requests.get ("https://jsonplaceholder.typicode.com/posts").json ()
    print(response.Text)
    print(response.Json()[0])
    assert len (response) == 100



