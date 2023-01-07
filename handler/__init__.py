from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder=".")

# Set up a database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/commands.db'
db = SQLAlchemy(app)
