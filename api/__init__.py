from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api.config import Configuration
from api.routes.home import home

db = SQLAlchemy()

def create_app():
    """
    A function that creates an instance of flask class

    Returns:
    --------
    app: instance of flask class
    """
    app = Flask(__name__)

    # Load configurations from config.py file
    app.config.from_object(Configuration)
    #deactivate auto sort for json keys
    app.json.sort_keys = False

    # Initialize db
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(home)

    # Create db models if not exists
    with app.app_context():
        db.create_all()

    return (app)
