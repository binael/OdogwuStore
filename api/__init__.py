from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from api.config import Configuration

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

    login_manager = LoginManager()
    login_manager.init_app(app)

    # Models for user loader
    from api.models import Seller
    from api.models import Product

    @login_manager.user_loader
    def load_user(user_id):
        if "role" in session and session.get("role") == "buyer":
            return Buyer.query.get(int(user_id))
        elif "role" in session and session.get("role") == "seller":
            return Seller.query.get(int(user_id))
        elif "role" in session and session.get("role") == "logistic":
            return Logistic.query.get(int(user_id))

    # Import blueprint routes
    from api.routes import buyer

    # Import blueprints for Sellers
    from api.routes import seller

    # Register blueprints
    app.register_blueprint(buyer)

    # Register blueprints for sellers
    app.register_blueprint(seller)

    # Create db models if not exists
    with app.app_context():
        db.create_all()

    return (app)
