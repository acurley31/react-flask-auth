from react_flask_auth.extensions import db
from react_flask_auth.database import Model


class User(Model):
    username = db.Column(db.String(), unique=True) 
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    is_active = db.Column(db.Boolean, default=True)
    password = db.Column(db.LargeBinary)
    password_salt = db.Column(db.LargeBinary)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'is_active': self.is_active,
        }  
