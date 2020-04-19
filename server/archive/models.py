from app import db


class Model(db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,
        default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())


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
            'date_created': self.date_created,
            'date_updated': self.date_updated,
        }


