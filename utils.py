import requests
import json
import numpy as np
from random import randint


def gen_user():
    return {
        'username': 'g' + ''.join([str(randint(0, 9)) for _ in range(7) ]),
        'password': '12345678',
        'email': 'gabriel.lins97@gmail.com',
    }

def request_user_creation(user):
    return requests.post(url=base_url+"users/create", data=user, headers=headers)

def request_user_login(user):
    return requests.post(url=base_url+"users/login", data=user, headers=headers)

def auth_master(token):
    headers = json.dumps({'Authorization': 'Bearer ' + token})
    return requests.get(url=base_url+"secret", headers=headers)

def get_user_token(username):
    user = gen_user()
    user['username'] = username
    user = json.dumps(user)
    print(request_user_creation(user).text)
    print(request_user_login(user).json())
    return request_user_login(user).json()['token']