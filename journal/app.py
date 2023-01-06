from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env")

app = Flask(__name__, template_folder=".")

# Set up a database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/journal.db'
db = SQLAlchemy(app)


# Define a model for Food entries
class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.BLOB, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Command %r>' % self.command


# Define a model for Water entries
class Water(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.BLOB, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Command %r>' % self.command


# Create the database tables if they don't already exist
with app.app_context():
    db.create_all()


def make_food(amount, name):
    new_entry = Food(amount=amount, name=name)

    db.session.add(new_entry)
    db.session.commit()

    return f'Food entry recorded: {amount} of {name}.'


def make_water(amount):
    new_entry = Water(amount=amount)

    db.session.add(new_entry)
    db.session.commit()

    return f'Water entry recorded: {amount}.'


# Set up a route to receive POST requests at the /commands endpoint
@app.route('/', methods=['GET', 'POST'])
def receive_command():
    if request.method == 'POST':
        # Get the JSON data from the request body
        data = request.get_json()

        # Access the data as a dictionary
        entry_type = data['type']
        amount = data['amount']
        name = data.get("name", "")

        match entry_type:
            case "food":
                response = make_food(amount, name)
            case "drink":
                response = make_water(amount)
            case _:
                response = f"Unknown command type {entry_type}; data not saved."

        return response

    # Get all commands from the database
    foods = Food.query.all()
    waters = Water.query.all()

    # Render the template with the commands
    return render_template('templates/commands.html', foods=foods, waters=waters)


@app.route('/food', methods=['GET', 'POST'])
def receive_command():
    if request.method == 'POST':
        # Get the JSON data from the request body
        data = request.get_json()

        # Access the data as a dictionary
        amount = data['amount']
        name = data.get("name", "")

        new_entry = Food(amount=amount, name=name)

        db.session.add(new_entry)
        db.session.commit()


def run_app():
    port = os.environ.get("JOURNAL_PORT")
    debug = os.environ.get("DEBUG")
    print(f"Running Journal on {port} {'in debug mode' if debug else ''}")
    app.run(port=port, debug=debug)


if __name__ == '__main__':
    run_app()

