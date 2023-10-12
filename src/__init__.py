from flask import Flask
from .routes.user_routes import user_routes
from flask_jwt_extended import JWTManager

app = Flask(__name__)
jwt = JWTManager(app)

def init_app(config):
    app.config.from_object(config)
    app.register_blueprint(user_routes)

    return app