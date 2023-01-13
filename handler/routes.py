import os
import requests
from flask import request, render_template, jsonify

from handler.models.command import Command
from dotenv import load_dotenv
from handler.models.ResponseMessage import ResponseMessage
from . import app, db


load_dotenv(dotenv_path="../.env")

# Create the database tables if they don't already exist
with app.app_context():
    db.create_all()


def send_message_and_receive_response(data, service_port):
    endpoint = f'http://{os.environ.get("SERVER_URL")}:{service_port}'
    print(endpoint)
    response: ResponseMessage = requests.post(url=endpoint, json=data).json()

    if response.success:
        return jsonify(response.message, 200)
    else:
        return jsonify(response.message, 400)


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
                service_port = os.environ.get("FEEDING_CALC_PORT")
                return send_message_and_receive_response(data, service_port)
            case "journal":
                service_port = os.environ.get("JOURNAL_PORT")
                return send_message_and_receive_response(data, service_port)
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

