from flask import request, render_template
import datetime
from dotenv import load_dotenv
import os

from journal.models.food import Food, make_food, get_foods
from journal.models.water import Water, make_water, get_waters
from .dataclasses.message import parse_request_data
from . import app

load_dotenv(dotenv_path="../.env")


@app.route('/', methods=['GET', 'POST'])
def all_data():

    # Get all entries from the database
    foods = Food.query.all()
    waters = Water.query.all()
    date = None

    if request.method == 'POST':
        # Get the JSON data from the request body
        if date := request.form.get('date'):
            date_str = datetime.datetime.strptime(date, '%Y-%m-%d')

            foods = get_foods(date_str)
            waters = get_waters(date_str)
            date = date_str

    # Render the template with the commands
    return render_template('templates/entryList.html', foods=foods, waters=waters, date=date)


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
        make_food(
            amount=request.form['amount'],
            name=request.form.get("name", "")
        )

    foods = Food.query.all()

    return render_template('templates/food.html', foods=foods)


@app.route('/water', methods=['GET', 'POST'])
def water():
    if request.method == 'POST':
        # Get the JSON data from the request body
        make_water(amount=request.form['amount'])

    waters = Water.query.all()

    return render_template('templates/water.html', waters=waters)


def run_app():
    port = os.environ.get("JOURNAL_PORT")
    debug = os.environ.get("DEBUG")
    print(f"Running Journal on {port} {'in debug mode' if debug else ''}")
    app.run(port=port, debug=debug)


if __name__ == '__main__':
    run_app()

