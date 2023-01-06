from flask import request, render_template

from common.models import ResponseMessage

from dotenv import load_dotenv
import os
from feeding_calc import app, db
from feeding_calc.models.VolumeRequest import VolumeRequest
from feeding_calc.models.NutramigenCalculation import NutramigenCalculation

load_dotenv(dotenv_path="../.env")


def save_volume_request(calories, volume):
    if not calories:
        return ResponseMessage(
            message='Missing Calorie Density',
            success=False
        )
    if not volume:
        return ResponseMessage(
            message='Missing Final Volume',
            success=False
        )

    new_entry = VolumeRequest(
        calorie_density=calories,
        final_volume=volume
    )

    db.session.add(new_entry)
    db.session.commit()

    return ResponseMessage(
        success=True,
        message=f"Successfully created Volume Request ({volume} @ {calories} cal)"
    )


@app.route('/', methods=['GET', 'POST'])
def allData():
    # Get the list of calculations from the database
    calculations = NutramigenCalculation.query.all()
    # Render the template and pass the calculations to the template context
    return render_template('index.html', calculations=calculations)


# Set up a route to receive POST requests at the /commands endpoint
@app.route('/message', methods=['GET', 'POST'])
def receive_command():
    if request.method == 'POST':
        # Get the JSON data from the request body
        data = request.get_json()

        calories = data['calories']
        volume = data['volume']

        # Create a new Command object and save it to the database
        save_request = save_volume_request(
            calories=calories,
            volume=volume
        )

        if save_request.success:
            formula_calc = NutramigenCalculation(
                calorie_density=calories,
                total_volume=volume
            )
            # calculate volume

            return ResponseMessage(
                success=True,
                message=f"{formula_calc.nutramigen_amount} g powder required to make {formula_calc.total_volume} @ {formula_calc.calorie_density} cal"
            )

        else:
            return save_request


def run_app():
    port = os.environ.get("FEEDING_CALC_PORT")
    debug = os.environ.get("DEBUG")
    print(f"Running Feeding Calc on {port} {'in debug mode' if debug else ''}")
    app.run(port=port, debug=debug)


if __name__ == '__main__':
    run_app()

