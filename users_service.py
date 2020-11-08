import requests
import json
from flask import jsonify, make_response

users_base_url = 'https://users-server-develop.herokuapp.com/'
# users_base_url = "http://users:5432/"


def login(email, password, path):
    response = requests.post(users_base_url + path,
                             data={"email": email, "password": password})

    if response.status_code == 200:
        return make_response(jsonify(json.loads(response.content)))
    elif response.status_code == 404:
        return make_response(jsonify(json.loads(response.content)), response.status_code)
    else:
        return make_response(response.content, response.status_code)


def register_user(email, password, name, surname, dni, user_type):
    response = requests.post(users_base_url + 'users',
                             data={"name": name, "surname": surname, "dni": dni, "email": email, "password": password,
                                   "type": user_type})
    return manage_register_response(response)


def register_admin(email, password, name, surname, dni):
    response = requests.post(users_base_url + 'admins',
                             data={"name": name, "surname": surname, "dni": dni, "email": email, "password": password})
    return manage_register_response(response)


def visualize_user(user_id, path):
    response = requests.get(users_base_url + path + user_id)
    return make_response(jsonify(json.loads(response.content)), response.status_code)


def manage_register_response(response):
    if response.status_code == 200:
        return make_response(jsonify(json.loads(response.content)))
    elif response.status_code == 409:
        return make_response(jsonify(json.loads(response.content)), response.status_code)
    else:
        return make_response(response.content, response.status_code)
