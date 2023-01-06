from flask import request, render_template, jsonify
import datetime
from dotenv import load_dotenv
import os

from journal.models.food import Food, make_food, get_foods
from journal.models.water import Water, make_water, get_waters
from .dataclasses.message import parse_request_data
from . import app, db

load_dotenv(dotenv_path="../.env")


@app.route('/', methods=['GET', 'POST'])
def all_data():
    if request.method == 'POST':
        # Get the JSON data from the request body
        data = request.get_json()

        date_str = data.get('date')

        date = None
        if date_str:
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d')

        foods = get_foods(date)
        waters = get_waters(date)

        return jsonify({
            'foods': foods,
            'waters': waters,
        })

    # Get all entries from the database
    foods = Food.query.all()
    waters = Water.query.all()

    # Render the template with the commands
    return render_template('templates/entryList.html', foods=foods, waters=waters)


# Set up a route to receive POST requests at the /commands endpoint
@app.route('/message', methods=['GET'])
def receive_message():
    if request.method == 'POST':
        # Get the JSON data from the request body
        message = parse_request_data(request.get_json())

        match message.entry_type:
            case "food":
                response = make_food(message.amount, message.name)
            case "drink":
                response = make_water(message.amount)
            case _:
                response = f"Unknown command type {message.entry_type}; data not saved."

        return response


@app.route('/food', methods=['GET', 'POST'])
def food():
    if request.method == 'POST':
        # Get the JSON data from the request body
        data = request.get_json()

        make_food(
            amount=data['amount'],
            name=data.get("name", "")
        )

    foods = Food.query.all()

    return render_template('templates/food.html', foods=foods)


@app.route('/water', methods=['GET', 'POST'])
def water():
    if request.method == 'POST':
        # Get the JSON data from the request body
        data = request.get_json()
        make_water(amount=data['amount'])

    waters = Water.query.all()

    return render_template('templates/water.html', waters=waters)


def run_app():
    port = os.environ.get("JOURNAL_PORT")
    debug = os.environ.get("DEBUG")
    print(f"Running Journal on {port} {'in debug mode' if debug else ''}")
    app.run(port=port, debug=debug)


if __name__ == '__main__':
    run_app()

