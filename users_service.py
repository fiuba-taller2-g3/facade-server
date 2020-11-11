import os
import requests
import json

from flask import jsonify, make_response

try:
    users_base_url = os.environ['USERS_URL']
except KeyError:
    users_base_url = 'https://users-server-develop.herokuapp.com/'


def login(email, password, path):
    response = requests.post(users_base_url + path,
                             data={"email": email, "password": password})

    if response.status_code == 200:
        return make_response(jsonify(json.loads(response.content)))
    elif response.status_code == 404:
        return make_response(jsonify(json.loads(response.content)), response.status_code)
    else:
        return make_response(response.content, response.status_code)


def register_user(email, password, name, surname, user_type):
    response = requests.post(users_base_url + 'users',
                             data={"name": name, "surname": surname, "email": email, "password": password,
                                   "type": user_type})
    return manage_register_response(response)


def register_admin(email, password, name, surname, dni):
    response = requests.post(users_base_url + 'admins',
                             data={"name": name, "surname": surname, "dni": dni, "email": email, "password": password})
    return manage_register_response(response)


def visualize_user(user_id, path, headers):
    if 'X-Auth-Token' in headers and 'X-Id' in headers:
        auth_header = headers['X-Auth-Token']
        id_header = headers['X-Id']
        headers = {'X-Auth-Token': auth_header, 'X-Id': id_header}
        response = requests.get(users_base_url + path + user_id, headers=headers)
        return make_response(jsonify(json.loads(response.content)), response.status_code)
    else:
        return make_response(jsonify({"error": "Request sin id y/o token de autorizacion"}), 400)


def visualize_users(path, headers):
    if 'X-Auth-Token' in headers and 'X-Id' in headers:
        auth_header = headers['X-Auth-Token']
        id_header = headers['X-Id']
        headers = {'X-Auth-Token': auth_header, 'X-Id': id_header}
        response = requests.get(users_base_url + path, headers=headers)
        return make_response(jsonify(json.loads(response.content)), response.status_code)
    else:
        return make_response(jsonify({"error": "Request sin id y/o token de autorizacion"}), 400)


def manage_register_response(response):
    if response.status_code == 200:
        return make_response(jsonify(json.loads(response.content)))
    elif response.status_code == 409:
        return make_response(jsonify(json.loads(response.content)), response.status_code)
    else:
        return make_response(response.content, response.status_code)
