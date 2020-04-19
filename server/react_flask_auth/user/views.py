from flask import Blueprint, request, jsonify
from react_flask_auth.database import db
from react_flask_auth.settings import SECRET_KEY
from react_flask_auth.decorators import requires_auth
from .models import User
from .validators import validate_user_create
from .utils import (
    hash_password, 
    create_password_salt,
    create_token,
    verify_token
)


blueprint = Blueprint('user', 
    __name__, 
    url_prefix='/api',
    static_folder='../static')


@blueprint.route('users', methods=['GET', 'POST'])
def user_list_create():
    if request.method == 'GET':
        return handle_get_users()
    else:
        data = dict(request.form)
        return handle_create_user(data)


def handle_get_users():
    '''Handle GET request to /users'''
    users = [user.serialize() for user in User.query.all()]
    return jsonify(users), 200


def handle_create_user(data):
    '''Handle POST request to /users'''

    if validate_user_create(data):
        password = data.pop('password2')
        password_salt = create_password_salt()
        hashed_password = hash_password(password, password_salt)
        data['password'] = hashed_password
        data['password_salt'] = password_salt
        user = User(**data)
        
        try:
            db.session.add(user)
            db.session.commit()
            return jsonify(user.serialize()), 201
        except:
            pass

    return jsonify({'detail': 'Invalid form data'}), 400


@blueprint.route('/users/<id>', methods=['GET', 'PATCH', 'DELETE'])
def user_detail(**kwargs):
    user_id = kwargs.get('id')
    if request.method == 'GET':
        return handle_get_user(user_id)

    elif request.method == 'PATCH':
        return handle_update_user(user_id, dict(request.form))

    elif request.method == 'DELETE':
        return handle_delete_user(user_id)


def handle_get_user(user_id):
    '''Handle GET request to /users/<id>'''
    user = User.query.get(user_id)
    if user:
        return jsonify(user.serialize()), 200
    return jsonify({'detail': 'User not found'}), 400


def handle_update_user(user_id, data):
    '''Hanlde PATCH request to /users/<id>'''
    user = User.query.get(user_id)
    if user:
        for attr in data:
            if attr not in ('username', 'password', 'password_salt'):
                setattr(user, attr, data[attr])
        db.session.commit()
        return jsonify(user.serialize()), 200

    return jsonify({'detail': 'Invalid request'}), 400


def handle_delete_user(user_id):
    '''Handle DELETE request to /users/<id>'''
    user = db.session.query(User).get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'id': user_id}), 200
    return jsonify({'detail': 'Invalid request'}), 400


@blueprint.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = db.session.query(User).filter(User.username==username).first()
    if user and user.password == hash_password(password, user.password_salt):
        token = create_token(SECRET_KEY)
        return jsonify({'token': token, 'id': user.id}), 200

    return jsonify({'detail': 'Invalid username or password'}), 401


@blueprint.route('/protected', methods=['GET'])
@requires_auth
def protected():
    
    return jsonify('protected route')
