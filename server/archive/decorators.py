from functools import wraps
from flask import jsonify, request
from utils import verify_token


def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if verify_token(token):
            return f(*args, **kwargs)
        return jsonify({'detail': 'unauthorized'}), 403 
    return wrapper
