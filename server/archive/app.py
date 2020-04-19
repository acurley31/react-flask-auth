from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import *
from views import *


app = Flask(__name__.split(".")[0])
app.config.from_object('config')


db = SQLAlchemy(app)
db.create_all()


if __name__ == '__main__':
    app.run()
