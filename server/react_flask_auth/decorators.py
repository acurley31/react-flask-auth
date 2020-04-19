from functools import wraps
from flask import jsonify, request
from react_flask_auth.settings import SECRET_KEY
from react_flask_auth.user.utils import verify_token


def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if verify_token(token, SECRET_KEY):
            return f(*args, **kwargs)
        return jsonify({'detail': 'Unauthorized request'}), 403 
    return wrapper
