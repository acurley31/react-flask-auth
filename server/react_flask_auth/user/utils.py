import os
import jwt
import hashlib
import datetime
from react_flask_auth.settings import TOKEN_EXPIRATION_SECONDS


def create_token(secret, payload={}, exp_seconds=TOKEN_EXPIRATION_SECONDS):
    '''Issue a token for a given payload'''
    
    now = datetime.datetime.utcnow()
    payload['iat'] = now.timestamp()
    payload['exp'] = payload['iat'] + exp_seconds
    token = jwt.encode(payload, secret, algorithm='HS256')
    return token.decode('utf-8')


def verify_token(token, secret):
    '''Check if a token is valid'''

    try:
        payload = jwt.decode(token.encode('utf-8'), secret)
        now = datetime.datetime.utcnow().timestamp()
        exp = payload['exp']
        return now < exp
    except:
        return False
    return False


def create_password_salt():
    '''Return a salt random salt value'''
    return os.urandom(32)


def hash_password(password, salt):
    '''Hash a password for secure storage'''
    
    return hashlib.pbkdf2_hmac('sha256', 
        password.encode('utf-8'),
        salt,
        100000,
        dklen=128)
