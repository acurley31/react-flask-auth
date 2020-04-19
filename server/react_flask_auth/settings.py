import os

# Update any settings
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///react_flask_auth.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get('SECRET_KEY')

# Token expiration
TOKEN_EXPIRATION_SECONDS = 5
