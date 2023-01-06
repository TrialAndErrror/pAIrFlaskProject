import os

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import json
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

app = Flask(__name__, template_folder=".")

# Set up a database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/commands.db'
db = SQLAlchemy(app)


# Define a model for the commands
class Command(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(200), nullable=False)
    data = db.Column(db.BLOB, nullable=False)

    def __init__(self, command, data):
        self.command = command
        self.data = json.dumps(data)

    @property
    def data(self):
        return json.loads(self.data_json)

    @data.setter
    def data(self, value):
        self.data_json = json.dumps(value)

    def __repr__(self):
        return '<Command %r>' % self.command


# Create the database tables if they don't already exist
with app.app_context():
    db.create_all()


# Set up a route to receive POST requests at the /commands endpoint
@app.route('/', methods=['GET', 'POST'])
def receive_command():
    if request.method == 'POST':
        # Get the JSON data from the request body
        data = request.get_json()

        # Access the data as a dictionary
        command = data['command']
        data = data['data']

        # Create a new Command object and save it to the database
        new_command = Command(command=command, data=data)
        db.session.add(new_command)
        db.session.commit()

        return 'Command received: %s' % command

    # Get all commands from the database
    commands = Command.query.all()

    # Render the template with the commands
    return render_template('templates/commands.html', commands=commands)


def run_app():
    port = os.environ.get("HANDLER_PORT")
    debug = os.environ.get("DEBUG")
    print(f"Running Handler on {port} {'in debug mode' if debug else ''}")
    app.run(port=port, debug=debug)


if __name__ == '__main__':
    run_app()

