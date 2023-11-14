"""
"""

import os
from datetime import timedelta


class Configuration:
    """
    List of all the configurations that is needed for the flask app
    """
    # Debug Configurations
    FLASK_DEBUG = True

    # General Configurations
    CSRF_ENABLED = True
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)

    # Key Configurations
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Database Configurations
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    # Uploaded Image Url
    UPLOADED_PHOTOS_DEST = os.environ.get("IMAGE_URL")
