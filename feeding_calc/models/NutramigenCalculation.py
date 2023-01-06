from .. import db


class NutramigenCalculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    calorie_density = db.Column(db.Float)
    total_volume = db.Column(db.Float)
    nutramigen_amount = db.Column(db.Float)

    def __init__(self, calorie_density, total_volume):
        self.calorie_density = calorie_density
        self.total_volume = total_volume
        # Calculate the amount of Nutramigen needed based on the calorie density and total volume
        self.nutramigen_amount = calc_nutramigen_amount(
            calories=calorie_density * total_volume,
            density=calorie_density,
            water_amount=total_volume
        )


def calc_nutramigen_amount(calories, density, water_amount):
    """Calculate the amount of Nutramigen powder needed to reach a specific calorie density.

    Parameters:
    calories (int): The desired number of calories.
    density (float): The desired calorie density (calories per mL).
    water_amount (float): The amount of water (in mL).

    Returns:
    float: The amount of Nutramigen powder needed (in grams).
    """
    # Nutramigen contains 20 calories per scoop (5.8 grams)
    scoops = calories / 20
    # Convert scoops to grams
    return scoops * 5.8 / (water_amount / density)
