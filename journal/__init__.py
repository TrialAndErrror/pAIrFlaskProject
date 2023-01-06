from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder=".", static_folder="./static")

# Set up a database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/journal.db'
db = SQLAlchemy(app)


# Create the database tables if they don't already exist
with app.app_context():
    db.create_all()
