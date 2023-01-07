from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__, template_folder="templates")

    # Set up a database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/commands.db'

    db = SQLAlchemy(app)

    return app, db


app, db = create_app()