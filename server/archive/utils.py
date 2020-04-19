import os
import hashlib


def create_token(payload={}, exp_seconds=5):
    return None


def verify_token(token):
    return False


def create_password_salt():
    return os.urandom(32)


def hash_password(password, salt):
    return None
