from flask import Flask
from .routes.machine_configuration_routes import machine_configuration_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(machine_configuration_bp)
    return app