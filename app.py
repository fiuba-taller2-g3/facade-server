import os
import json
import requests
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

users_base_url = 'https://users-server-develop.herokuapp.com/'


def login_user(email, password):
    response = requests.post(users_base_url + 'users/login',
                             data={"email": email, "password": password})

    if response.status_code == 200:
        return jsonify({"msg": json.loads(response.content)['msg'], "api_token": json.loads(response.content)['api_token']})
    elif response.status_code == 404:
        return make_response(jsonify({"error": json.loads(response.content)['error']}), 404)
    else:
        return make_response(response.content, 500)


def login_admin(email, password):
    response = requests.post(users_base_url + 'admins/login',
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


@app.route('/')
def hello():
    return 'Hello World!\n'


@app.route('/users/login', methods=['POST'])
def users_login():
    content = request.json
    email = content.get('email')
    password = content.get('password')

    return login_user(email, password)


@app.route('/admins/login', methods=['POST'])
def admins_login():
    content = request.json
    email = content.get('email')
    password = content.get('password')

    return login_admin(email, password)


@app.route('/users', methods=['POST'])
def users_register():
    content = request.json
    email = content.get('email')
    password = content.get('password')
    name = content.get('name')
    surname = content.get('surname')
    dni = content.get('dni')
    user_type = content.get('huesped')

    return register_user(email, password, name, surname, dni, user_type)


@app.route('/admins', methods=['POST'])
def admins_register():
    content = request.json
    email = content.get('email')
    password = content.get('password')
    name = content.get('name')
    surname = content.get('surname')
    dni = content.get('dni')

    return register_admin(email, password, name, surname, dni)


if __name__ == '__main__':
    try:
        users_base_url = os.environ['USERS_URL']
        app.run(port=os.environ['PORT'])
    except KeyError:
        app.run()
