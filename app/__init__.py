from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# ✅ Create shared instances here
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'devkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register routes AFTER db is initialized
    from .routes import inventory_bp
    app.register_blueprint(inventory_bp)

    return app
