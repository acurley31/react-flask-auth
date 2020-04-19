from flask import Flask, render_template
from react_flask_auth.extensions import db
from react_flask_auth import user


def create_app(config_obj='react_flask_auth.settings'):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_obj)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

def register_blueprints(app):
    app.register_blueprint(user.views.blueprint)
        


