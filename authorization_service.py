from datetime import datetime, timedelta
import jwt

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 1200

admins = {}
users = {}


def create_token(login_response):
    login_response['exp'] = datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
    return jwt.encode(login_response, JWT_SECRET, JWT_ALGORITHM)


def generate_user_token(login_response):
    token = create_token(login_response)
    decoded_token = jwt.decode(token, 'secret', algorithms=[JWT_ALGORITHM])
    print("decoded token", decoded_token)
    user_id = decoded_token['id']
    users[user_id] = token
    return token.decode()


def generate_admin_token(login_response):
    token = create_token(login_response)
    decoded_token = jwt.decode(token, 'secret', algorithms=[JWT_ALGORITHM])
    print("decoded token", decoded_token)
    admin_id = decoded_token['id']
    admins[admin_id] = token
    return token.decode()


def verify_user_token(token):
    try:
        decoded_token = jwt.decode(token, 'secret', algorithms=[JWT_ALGORITHM])
        user_id = decoded_token['id']
        if user_id in users.keys():
            return users[user_id].decode() == token
        return False
    except jwt.exceptions.DecodeError:
        return False


def verify_admin_token(token):
    try:
        decoded_token = jwt.decode(token, 'secret', algorithms=[JWT_ALGORITHM])
        admin_id = decoded_token['id']
        if admin_id in admins.keys():
            return admins[admin_id].decode() == token
        return False
    except jwt.exceptions.DecodeError:
        return False


def admins_is_empty():
    return not bool(admins)
