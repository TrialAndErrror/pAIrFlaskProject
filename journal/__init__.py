from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates", static_folder="static")

# Set up a database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@journal_db:5432/postgres'
db = SQLAlchemy(app)



