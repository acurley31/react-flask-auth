import os
import jwt
import hashlib
import datetime


def create_token(secret, payload={}, exp_seconds=5):
    '''Issue a token for a given payload'''
    
    now = datetime.datetime.utcnow()
    payload['iat'] = now.timestamp()
    payload['exp'] = payload['iat'] + exp_seconds
    token = jwt.encode(payload, secret, algorithm='HS256')
    return token.encode('utf-8')


def verify_token(token):
    '''Check if a token is valid'''

    print(token)
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
