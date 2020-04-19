from flask import Blueprint, request, jsonify
from react_flask_auth.database import db
from .models import User
from .validators import validate_user_create
from .utils import hash_password, create_password_salt


blueprint = Blueprint('user', 
    __name__, 
    url_prefix='/api/users',
    static_folder='../static')


@blueprint.route('', methods=['GET', 'POST'])
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


@blueprint.route('/<id>', methods=['GET', 'PATCH', 'DELETE'])
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
