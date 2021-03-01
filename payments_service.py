import os
import requests
import json
import jwt
from flask import jsonify, make_response, request
from users_service import verify_user_token, verify_admin_token

try:
    payments_base_url = os.environ['PAYMENTS_URL']
except KeyError:
    payments_base_url = 'https://payments-server-develop.herokuapp.com/'

def transfer():
    try:
        if verify_admin_token(request.headers['API_TOKEN']):
            print(payments_base_url + request.full_path[1:])
            print(request.json)
            response = requests.post(payments_base_url + request.full_path[1:], json=request.json)
            return response.content
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)

def balance():
    try:
        if verify_admin_token(request.headers['API_TOKEN']):
            print(payments_base_url + request.full_path[1:])
            print(request.json)
            response = requests.get(payments_base_url + request.full_path[1:].replace("users", "identity"))
            return response.content
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)

def transactions():
    try:
        if verify_admin_token(request.headers['API_TOKEN']):
            print(payments_base_url + request.full_path[1:])
            print(request.json)
            response = requests.get(payments_base_url + request.full_path[1:].replace("users", "identity"))
            return response.content
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)
