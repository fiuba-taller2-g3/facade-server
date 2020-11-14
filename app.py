from flask import Flask, request

from users_service import login, register_user, register_admin, visualize_user, visualize_users, block_user

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!\n'


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

    return register_user(email, password, name, surname, user_type)


@app.route('/admins', methods=['POST'])
def admins_register():
    content = request.json
    email = content.get('email')
    password = content.get('password')
    name = content.get('name')
    surname = content.get('surname')
    dni = content.get('dni')

    return register_admin(email, password, name, surname, dni)


@app.route('/users/<user_id>')
def user_visualization(user_id):
    return visualize_user(user_id, 'users/', request.headers)


@app.route('/users')
def users_visualization():
    return visualize_users('users', request.headers)


@app.route('/users/<user_id>', methods=['PUT'])
def users_block(user_id):
    content = request.json
    return block_user(user_id, 'users/', request.headers, content.get("is_blocked"))


if __name__ == '__main__':
    try:
        app.run(port=os.environ['PORT'])
    except KeyError:
        app.run()
