from flask import Flask
from .routes.repair_routes import repair_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(repair_bp)
    return app