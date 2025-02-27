from flask import Flask
from .routes import main
import os

def create_app():
    app = Flask(__name__)
    
    # Register the Blueprint
    app.register_blueprint(main)
    app.config['SECRET_KEY'] = os.urandom(24)

    return app

