import requests
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

users_base_url = 'https://users-server-develop.herokuapp.com/'

def login(email, password):
    response = requests.post(users_base_url + 'users/login',
                             data={"username": email, "password": password})

    print("response:", response.content)

    if response.status_code == 200:
        return jsonify({"msg": "Usuario logueado exitosamente"})
    elif response.status_code == 404:
        return make_response(jsonify({"msg": "Usuario y/o contraseña invalidos"}), 404)
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

    return login(email, password)


@app.route('/admins/login', methods=['POST'])
def admins_login():
    content = request.json
    email = content.get('email')
    password = content.get('password')

    return login(email, password)


if __name__ == '__main__':
    try:
        app.run(port = os.environ['PORT'])
        users_base_url = os.environ['USERS_URL']
    except KeyError:
        app.run()
