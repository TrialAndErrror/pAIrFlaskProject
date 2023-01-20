import os
import requests
from flask import request, render_template, jsonify

from handler.models.command import Command
from dotenv import load_dotenv
from . import app, db


load_dotenv(dotenv_path="../.env")

# Create the database tables if they don't already exist
with app.app_context():
    db.create_all()


def send_message_and_receive_response(data, service: str):
    endpoint = f'http://{service}:8000'
    response = requests.post(url=endpoint, json=data)
    print(response)
    print(response.json())
    response_data: dict = response.json()

    if response_data.get('success'):
        return jsonify(response_data.get('message'), 200)
    else:
        return jsonify(response_data.get('message'), 400)


# Set up a route to receive POST requests at the /commands endpoint
@app.route('/', methods=['GET', 'POST'])
def receive_command():
    """ Receive command and dispatch accordingly"""

    """
    Command Format:
        {
            'command': 'calc' | 'journal'
            'data': {}
        }
        
    Calc Data:
        {
            'calories': float
            'volume': float
        }
        
    Journal Data:
        {
            'entry_type': str
            'amount': float
            'name': str
        }
    """

    if request.method == 'POST':
        # Get the JSON data from the request body
        data = request.get_json()

        # Access the data as a dictionary
        command = data.pop('command')

        # Create a new Command object and save it to the database
        new_command = Command(command=command, data=data)
        db.session.add(new_command)
        db.session.commit()

        match command:
            case "calc":
                service = "feeding_calc"
                return send_message_and_receive_response(data, service)
            case "journal":
                service = "journal"
                return send_message_and_receive_response(data, service)
            case "_":
                return f'Unknown Command received: {command}'

    # Get all commands from the database
    commands = Command.query.all()

    # Render the template with the commands
    return render_template('commands.html', commands=commands)


def run_app():
    port = os.environ.get("HANDLER_PORT")
    debug = os.environ.get("DEBUG")
    print(f"Running Handler on {port} {'in debug mode' if debug else ''}")
    app.run(port=port, debug=debug)


if __name__ == '__main__':
    run_app()

