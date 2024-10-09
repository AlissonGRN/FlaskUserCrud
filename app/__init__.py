from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # TODO  Adcionar e configurar JWT 

    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import init_routes
    init_routes(app)

    return app