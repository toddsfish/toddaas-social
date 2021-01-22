#!/bin/bash
source venv/bin/activate
export FLASK_APP=application.py
export FLASK_ENV=development
export SECRET_KEY='fu?\b#!bOs6j1@vK?==5s=\?1GmOVBO6'
flask run --host '0.0.0.0' --port 8080
