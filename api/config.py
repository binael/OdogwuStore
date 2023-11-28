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

    # Flask Mail Configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEBUG = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = "O-STORE"
    MAIL_MAX_EMAILS = None
    MAIL_SUPPRESS_SENDER = False
    MAIL_ASCII_ATTACHMENTS = False
