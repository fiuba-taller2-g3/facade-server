import requests
import json
from flask import jsonify, make_response

users_base_url = 'https://users-server-develop.herokuapp.com/'


def login(email, password, path):
    response = requests.post(users_base_url + path,
                             data={"email": email, "password": password})

    if response.status_code == 200:
        return jsonify({"msg": json.loads(response.content)['msg'], "api_token": json.loads(response.content)['api_token']})
    elif response.status_code == 404:
        return make_response(jsonify({"error": json.loads(response.content)['error']}), 404)
    else:
        return make_response(response.content, 500)


def register_user(email, password, name, surname, dni, user_type):
    response = requests.post(users_base_url + 'users',
                             data={"name": name, "surname": surname, "dni": dni, "email": email, "password": password,
                                   "type": user_type})
    if response.status_code == 200:
        return make_response(jsonify(json.loads(response.content)))
    elif response.status_code == 409:
        return make_response(jsonify(json.loads(response.content)), 409)
    else:
        return make_response(response.content, 500)


def register_admin(email, password, name, surname, dni):
    response = requests.post(users_base_url + 'admins',
                             data={"name": name, "surname": surname, "dni": dni, "email": email, "password": password})
    if response.status_code == 200:
        return make_response(jsonify(json.loads(response.content)))
    elif response.status_code == 409:
        return make_response(jsonify(json.loads(response.content)), 409)
    else:
        return make_response(response.content, 500)