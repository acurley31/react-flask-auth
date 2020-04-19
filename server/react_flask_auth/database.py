from react_flask_auth.extensions import db


class Model(db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
