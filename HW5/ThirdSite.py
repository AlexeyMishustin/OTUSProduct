import json

import requests,random,pytest

def test_check_active_site():
    request = requests.get('https://jsonplaceholder.typicode.com/')
    assert request.status_code == 200, "Check by 200 status for site"

def test_get_posts():
    request = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert request.status_code == 200, "Check url for get request"

def test_get_select_post():
    ID = random.randint(1,10)
    request = requests.get(f'https://jsonplaceholder.typicode.com/posts/{ID}')
    assert request.json()['id'] == ID, f'Check ID for randomint, where ID = {ID}'

@pytest.mark.parametrize("ID",(1,5,7,10))
def test_get_select_post(ID):
    request = requests.get(f'https://jsonplaceholder.typicode.com/posts/{ID}')
    assert request.json()['id'] == ID, f'Check ID for randomint, where ID = {ID}'

def test_post_request_from_post():
    Data = {"userId" : random.randint(50,100),
            "id" : random.randint(50,100),
            "title" : "test",
            "body" : "this is test"}
    request = requests.post(url='https://jsonplaceholder.typicode.com/posts',data=Data)
    assert request.status_code == 201

@pytest.mark.parametrize("data", [
    ({"userId": 21, "id": 21, "title": "test", "body": "test1"}),
    ({"userId": 27, "id": 21, "title": "notest", "body": "notest1"})
])
def test_post_request_from_post(data):
    request = requests.post(url='https://jsonplaceholder.typicode.com/posts',data=data)
    assert request.status_code == 201