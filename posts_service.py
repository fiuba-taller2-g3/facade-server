import os
import requests
import json
from flask import jsonify, make_response, request

try:
    posts_base_url = os.environ['POSTS_URL']
except KeyError:
    posts_base_url = 'https://posts-server-develop.herokuapp.com/'

def new(req):
    response = requests.post(posts_base_url + request.full_path, json=request.json)
    return response.content

def visualize(request):
    response = requests.get(posts_base_url + request.full_path)
    return response.content

def edit(request):
    response = requests.patch(posts_base_url + request.full_path, json=request.json)
    return response.content

def delete(request):
    response = requests.delete(posts_base_url + request.full_path)
    return response.content

def visualize_from_user(request):
    response = requests.get(posts_base_url + request.full_path)
    return response.content

def reset(request):
    response = requests.delete(posts_base_url + request.full_path)
    return response.content
