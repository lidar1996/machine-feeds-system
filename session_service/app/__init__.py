from flask import Flask
from .routes.session_routes import session_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(session_bp)
    return app