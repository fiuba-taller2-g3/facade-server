import os
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from posts_service import *
from users_service import login, register_user, register_admin, visualize_user, visualize_users, block_user, update_user
from authorization_service import admins_is_empty

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello World!\n'

@app.route('/posts/reset', methods=['DELETE'])
def reset_posts():
    return reset(request)

@app.route('/posts', methods=['POST'])
def new_post():
    return new(request)

@app.route('/posts/<post_id>')
def visualize_post(post_id):
    return visualize(request)

@app.route('/posts/<post_id>', methods=['PATCH'])
def edit_post(post_id):
    return edit(request)

@app.route('/posts/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    return delete(request)

@app.route('/posts')
def visualize_posts_from_user():
    return visualize_from_user(request)


@app.route('/users/login', methods=['POST'])
def users_login():
    content = request.json
    email = content.get('email')
    password = content.get('password')

    return login(email, password, "users/login")


@app.route('/admins/login', methods=['POST'])
def admins_login():
    content = request.json
    email = content.get('email')
    password = content.get('password')

    return login(email, password, "admins/login")


@app.route('/users', methods=['POST'])
def users_register():
    content = request.json
    email = content.get('email')
    password = content.get('password')
    name = content.get('name')
    surname = content.get('surname')
    user_type = content.get('type')
    phone_number = content.get('phone_number')
    gender = content.get('gender')
    birth_date = content.get('birth_date')

    return register_user(email, password, name, surname, user_type, phone_number, gender, birth_date)


@app.route('/admins', methods=['POST'])
def admins_register():
    if 'API_TOKEN' in request.headers or admins_is_empty():
        api_token = request.headers['API_TOKEN']
        content = request.json
        email = content.get('email')
        password = content.get('password')
        name = content.get('name')
        surname = content.get('surname')
        dni = content.get('dni')
        return register_admin(email, password, name, surname, dni, api_token)
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


@app.route('/users/<user_id>')
def user_visualization(user_id):
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return visualize_user(user_id, 'users/', api_token)
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


@app.route('/users')
def users_visualization():
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return visualize_users('users', api_token)
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


@app.route('/users/<user_id>', methods=['PATCH'])
def users_block(user_id):
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return block_user(user_id, 'users/', api_token, request.json.get("is_blocked"))
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


@app.route('/users/<user_id>', methods=['PUT'])
def users_update(user_id):
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return update_user(user_id, 'users/', api_token, request.json)
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


if __name__ == '__main__':
    try:
        app.run(port=os.environ['PORT'])
    except KeyError:
        app.run()
