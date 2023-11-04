"""
"""

import os


class Configuration:
    """
    List of all the configurations that is needed for the flask app
    """
    # Debug Configurations
    FLASK_DEBUG = True

    # General Configurations
    CSRF_ENABLED = True

    # Key Configurations
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Database Configurations
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
