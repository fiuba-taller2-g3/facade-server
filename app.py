import requests, json
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


def login_user(email, password):
    response = requests.post('https://users-server-develop.herokuapp.com/users/login',
                             data={"email": email, "password": password})

    print("response:", response.content)

    if response.status_code == 200:
        return jsonify({"msg": "Usuario logueado exitosamente", "api_token": json.loads(response.content)['api_token']})
    elif response.status_code == 404:
        return make_response(jsonify({"msg": "Usuario y/o contraseña invalidos"}), 404)
    else:
        return response.content


def login_admin(email, password):
    response = requests.post('https://users-server-develop.herokuapp.com/admins/login',
                             data={"email": email, "password": password})

    print("response:", json.loads(response.content))

    if response.status_code == 200:
        return jsonify({"msg": "Administrador logueado exitosamente", "api_token": json.loads(response.content)['api_token']})
    elif response.status_code == 404:
        return make_response(jsonify({"msg": "Usuario y/o contraseña invalidos"}), 404)
    else:
        return response.content


def register_user(email, password, name, surname, dni, user_type):
    response = requests.post('https://users-server-develop.herokuapp.com/users',
                             data={"name": name, "surname": surname, "dni": dni, "email": email, "password": password,
                                   "type": user_type})
    if response.status_code == 200:
        return jsonify({"msg": "Usuario registrado exitosamente"})
    else:
        return response.content


def register_admin(email, password, name, surname, dni):
    response = requests.post('https://users-server-develop.herokuapp.com/admins',
                             data={"name": name, "surname": surname, "dni": dni, "email": email, "password": password})
    if response.status_code == 200:
        return jsonify({"msg": "Administrador registrado exitosamente"})
    else:
        return response.content


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!\n' % name


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
    app.run()
