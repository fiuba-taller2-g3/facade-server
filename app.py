import os
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from posts_service import *
from payments_service import *
from users_service import login, register_user, register_admin, visualize_user, visualize_users, block_user, \
    update_user, register_fb_user, login_fb
from authorization_service import admins_is_empty

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return 'Hello World!\n'


@app.route('/transference', methods=['POST'])
def transfer_funds():
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return transfer()
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)

@app.route('/users/<wallet_id>/balance', methods=['GET'])
def get_balance(wallet_id):
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return balance()
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)

@app.route('/users/<wallet_id>/transactions', methods=['GET'])
def get_transactions(wallet_id):
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return transactions()
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


@app.route('/feedback', methods=['POST'])
def new_feedback():
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return new_feed()
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


@app.route('/feedback')
def search_feedback():
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return search_feed()
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


@app.route('/posts', methods=['DELETE'])
def reset_posts():
    return reset()


@app.route('/posts', methods=['POST'])
def new_post():
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return new()
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


@app.route('/posts/<post_id>')
def visualize_post(post_id):
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return visualize()
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


@app.route('/posts/<post_id>', methods=['PATCH'])
def edit_post(post_id):
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return edit()
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


@app.route('/posts/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return delete()
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


@app.route('/posts')
def search_posts():
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return search()
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


@app.route('/bookings', methods=['GET'])
def get_booking():
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return get_bookings()
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


@app.route('/bookings', methods=['POST'])
def new_booking():
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return create_new_booking()
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


@app.route('/acceptance', methods=['POST'])
def new_accept_booking():
    if 'API_TOKEN' in request.headers:
        api_token = request.headers['API_TOKEN']
        return accept_booking()
    else:
        return make_response(jsonify({"error": "Request sin token de autorizacion"}), 400)


@app.route('/users/login', methods=['POST'])
def users_login():
    content = request.json
    email = content.get('email')
    password = content.get('password')

    return login(email, password, "users/login")


@app.route('/users/login_fb', methods=['POST'])
def users_login_fb():
    content = request.json
    email = content.get('email')
    fb_id = content.get('id')

    return login_fb(email, fb_id)


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
    phone_number = content.get('phone_number')
    gender = content.get('gender')
    birth_date = content.get('birth_date')

    return register_user(email, password, name, surname, phone_number, gender, birth_date)


@app.route('/fb/users', methods=['POST'])
def users_register_fb():
    content = request.json
    fb_id = content.get('id')
    name = content.get('name')
    surname = content.get('surname')
    email = content.get('email')
    phone_number = content.get('phone_number')
    gender = content.get('gender')
    birth_date = content.get('birth_date')

    return register_fb_user(email, fb_id, name, surname, phone_number, gender, birth_date)


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


@app.route('/notifications', methods=['POST'])
def notifications():
    user_id = request.args.get('user_id')
    response = requests.post(posts_base_url + "notifications?user_id=" + user_id)
    return response.content


@app.route('/tokens', methods=['POST'])
def save_token():
    response = requests.post(posts_base_url + "tokens", json=request.json)
    return response.content


@app.route('/posts/metrics')
def posts_for_metrics():
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')
    response = requests.get(posts_base_url + "posts/metrics?from_date=" + from_date + "&to_date=" + to_date)
    return response.content


if __name__ == '__main__':
    try:
        app.run(port=os.environ['PORT'])
    except KeyError:
        app.run()
