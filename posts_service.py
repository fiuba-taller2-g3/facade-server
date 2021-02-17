import os
import requests
import json
import jwt
from flask import jsonify, make_response, request
from users_service import verify_user_token, verify_admin_token

try:
    posts_base_url = os.environ['POSTS_URL']
except KeyError:
    posts_base_url = 'https://posts-server-develop.herokuapp.com/'

def new():
    try:
        if verify_user_token(request.headers['API_TOKEN']):
            response = requests.post(posts_base_url + request.full_path, json=request.json)
            return response.content
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)


def visualize():
    try:
        if verify_user_token(request.headers['API_TOKEN']) or verify_admin_token(request.headers['API_TOKEN']):
            response = requests.get(posts_base_url + request.full_path)
            return response.content
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)

def edit():
    try:
        if verify_user_token(request.headers['API_TOKEN']) or verify_admin_token(request.headers['API_TOKEN']):
            response = requests.patch(posts_base_url + request.full_path, json=request.json)
            return response.content
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)

def delete():
    try:
        if verify_user_token(request.headers['API_TOKEN']):
            response = requests.delete(posts_base_url + request.full_path)
            return response.content
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)

def search():
    try:
        if verify_user_token(request.headers['API_TOKEN']) or verify_admin_token(request.headers['API_TOKEN']):
            response = requests.get(posts_base_url + request.full_path)
            return response.content
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)

def create_new_booking():
    try:
        if verify_user_token(request.headers['API_TOKEN']):
            response = requests.post(posts_base_url + request.full_path, json=request.json)
            return response.content
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)

def accept_booking():
    try:
        if verify_user_token(request.headers['API_TOKEN']):
            response = requests.post(posts_base_url + request.full_path, json=request.json)
            return response.content
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)

def get_bookings():
    try:
        if verify_user_token(request.headers['API_TOKEN']):
            response = requests.get(posts_base_url + request.full_path, json=request.json)
            return response.content
        else:
            return make_response(jsonify({"error": "No estas autorizado para hacer este request"}), 401)
    except jwt.exceptions.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token expirado, debe loguearse de nuevo"}), 401)

def reset():
    response = requests.delete(posts_base_url + request.full_path)
    return response.content
