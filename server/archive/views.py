from flask import request, jsonify
from app import app
from models import *
from decorators import requires_auth
from utils import (
    create_password_salt,
    hash_password, 
    create_token, 
    verify_token
)


@app.route('/')
def index():
    return jsonify({ 'detail': 'index.html' }), 200


@app.route('/api/users')
def user_list_create():
    return 


@app.route('/api/users/<id>')
def user_detail():
    return


@app.route('/api/login')
def login():
    return



