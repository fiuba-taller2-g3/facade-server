from flask import Flask, request

from users_service import login

app = Flask(__name__)


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
    app.run()
