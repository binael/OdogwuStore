#!/usr/bin/env bash

# exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

# Use this in the render settings
# export PATH=$PATH:/usr/local/python3/bin && pip install gunicorn && gunicorn app:app
