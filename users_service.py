import os

import jwt
import requests
import json

from flask import jsonify, make_response
from authorization_service import generate_user_token, generate_admin_token, verify_user_token, verify_admin_token, admins_is_empty

try:
    users_base_url = os.environ['USERS_URL']
except KeyError:
    users_base_url = 'https://users-server-develop.herokuapp.com/'

def login(email, password, path):
    response = requests.post(users_base_url + path,
                             data={"email": email, "password": password})

    if response.status_code == 200:
        if 'users' in path:
            token = generate_user_token(json.loads(response.content))
        else:
            token = generate_admin_token(json.loads(response.content))

        return make_response(jsonify({"api_token": token}))
    elif response.status_code == 404:
        return make_response(jsonify(json.loads(response.content)), response.status_code)
    else:
        return make_response(response.content, response.status_code)


def register_user(email, password, name, surname, phone_number, gender, birth_date):
    response = requests.post(users_base_url + 'users',
                             data={"name": name, "surname": surname, "email": email, "password": password,
                                   "phone_number": phone_number, "gender": gender, "birth_date": birth_date})
    return manage_register_response(response)


def register_admin(email, password, name, surname, dni, api_token):
    try:
        if verify_admin_token(api_token) or admins_is_empty():
            response = requests.post(users_base_url + 'admins',
                                     data={"name": name, "surname": surname, "dni": dni, "email": email, "password": password})
            return manage_register_response(response)
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)


def visualize_user(user_id, path, api_token):
    try:
        if verify_user_token(api_token) or verify_admin_token(api_token):
            response = requests.get(users_base_url + path + user_id)
            return make_response(jsonify(json.loads(response.content)), response.status_code)
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)


def visualize_users(path, api_token):
    try:
        if verify_admin_token(api_token):
            response = requests.get(users_base_url + path)
            return make_response(jsonify(json.loads(response.content)), response.status_code)
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)


def block_user(user_id, path, api_token, is_blocked):
    try:
        if verify_admin_token(api_token):
            response = requests.patch(users_base_url + path + user_id, data={"is_blocked": is_blocked})
            return make_response(jsonify(json.loads(response.content)), response.status_code)
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)


def update_user(user_id, path, api_token, body):
    try:
        if verify_user_token(api_token):
            response = requests.put(users_base_url + path + user_id, data={"name": body.get("name"),
                                                                           "surname": body.get("surname"),
                                                                           "email": body.get("email"),
                                                                           "phone_number": body.get("phone_number"),
                                                                           "gender": body.get("gender"),
                                                                           "birth_date": body.get("birth_date")})
            return make_response(jsonify(json.loads(response.content)), response.status_code)
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)


def manage_register_response(response):
    if response.status_code == 200:
        return make_response(jsonify(json.loads(response.content)))
    elif response.status_code == 409:
        return make_response(jsonify(json.loads(response.content)), response.status_code)
    else:
        return make_response(response.content, response.status_code)
