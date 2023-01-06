from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


app = Flask(__name__, template_folder="./templates", static_folder="./static")

# Set up a database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/feeding_calc.db'
db.init_app(app)

with app.app_context():
    db.create_all()

