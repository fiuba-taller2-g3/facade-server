import requests
from flask import jsonify, make_response


def login(email, password):
    response = requests.post('https://users-server-develop.herokuapp.com/users/login',
                             data={"username": email, "password": password})

    print("response:", response.content)

    if response.status_code == 200:
        return jsonify({"msg": "Usuario logueado exitosamente"})
    elif response.status_code == 404:
        return make_response(jsonify({"msg": "Usuario y/o contraseña invalidos"}), 404)
    else:
        return response.content