from flask import Flask
from .routes.machine_feeds_routes import machine_feeds_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(machine_feeds_bp)
    return app